from flask import jsonify, request
from models.user import UserModel
from models.album import AlbumModel
import logging

logger = logging.getLogger(__name__)

class PaymentGatewayController:

    @staticmethod
    def process_store_purchase():
        """Maneja el flujo de cobro para recargas, sobres y álbumes."""
        try:
            datos = request.get_json()

            # Debug temporal
            print(">>> BODY RECIBIDO:", datos)
            print(">>> Content-Type:", request.content_type)

            usuario_id = datos.get('usuario_id') if datos else None
            tipo_item  = datos.get('tipo_item')  if datos else None
            monto      = datos.get('monto')      if datos else None

            print(">>> usuario_id:", usuario_id)
            print(">>> tipo_item:", tipo_item)
            print(">>> monto:", monto)

            if not all([usuario_id, tipo_item, monto]):
                return jsonify({"error": "Información de compra incompleta"}), 400

            monto = float(monto)
            if monto <= 0:
                return jsonify({"error": "El monto debe ser mayor a 0"}), 400

            # ─────────────────────────────────────────
            # CASO 1: RECARGA (crédito, no requiere saldo previo)
            # ─────────────────────────────────────────
            if tipo_item == 'recarga':
                exito = UserModel.update_balance(usuario_id, monto)
                if exito:
                    saldo_nuevo = UserModel.get_user_balance(usuario_id)
                    return jsonify({
                        "mensaje": "Recarga exitosa",
                        "monto_recargado": monto,
                        "nuevo_saldo": saldo_nuevo
                    }), 200
                return jsonify({"error": "No se pudo procesar la recarga"}), 500

            # ─────────────────────────────────────────
            # CASO 2 y 3: COMPRAS (requieren saldo suficiente)
            # ─────────────────────────────────────────
            saldo_actual = UserModel.get_user_balance(usuario_id)

            if saldo_actual is None:
                return jsonify({"error": "Usuario no encontrado"}), 404

            if saldo_actual < monto:
                return jsonify({
                    "error": "Saldo insuficiente",
                    "saldo_actual": saldo_actual,
                    "monto_requerido": monto
                }), 400

            # Débito atómico (protegido contra saldo negativo en la BD)
            debito_exitoso = UserModel.update_balance(usuario_id, -monto)
            if not debito_exitoso:
                return jsonify({"error": "No se pudo procesar el débito"}), 500

            nuevo_saldo = saldo_actual - monto

            # CASO 2: SOBRE
            if tipo_item == 'sobre':
                resultado = AlbumModel.open_pack(usuario_id)
                if resultado:
                    return jsonify({
                        "mensaje": "Sobre comprado y abierto exitosamente",
                        "laminas_obtenidas": resultado,
                        "nuevo_saldo": nuevo_saldo
                    }), 200

            # CASO 3: ÁLBUM
            elif tipo_item == 'album':
                success = AlbumModel.activate_album(usuario_id)
                if success:
                    return jsonify({
                        "mensaje": "Álbum adquirido exitosamente",
                        "nuevo_saldo": nuevo_saldo
                    }), 200

            # CASO 4: Tipo no reconocido
            else:
                # Reembolso inmediato si el tipo no existe
                UserModel.update_balance(usuario_id, monto)
                return jsonify({
                    "error": f"Tipo de item '{tipo_item}' no reconocido. Cobro revertido."
                }), 400

            # Si llegamos aquí: cobro OK pero entrega falló → reembolso automático
            logger.critical(
                f"[CRITICO] Cobro exitoso pero falla en entrega | "
                f"usuario={usuario_id} tipo={tipo_item} monto={monto}"
            )
            UserModel.update_balance(usuario_id, monto)
            return jsonify({
                "error": "No se pudo entregar el ítem. El cobro fue revertido automáticamente."
            }), 500

        except Exception as e:
            logger.error(f"Error en pasarela de pagos: {str(e)}")
            return jsonify({"error": f"Error en el servidor: {str(e)}"}), 500

    @staticmethod
    def simulate_bet():
        """Simula una transacción de apuesta."""
        try:
            datos         = request.get_json()
            usuario_id    = datos.get('usuario_id')    if datos else None
            monto_apuesta = datos.get('monto')         if datos else None

            if not usuario_id or not monto_apuesta:
                return jsonify({"error": "Datos de apuesta inválidos"}), 400

            monto_apuesta = float(monto_apuesta)
            if monto_apuesta <= 0:
                return jsonify({"error": "El monto de apuesta debe ser mayor a 0"}), 400

            # Verificar usuario y saldo
            saldo = UserModel.get_user_balance(usuario_id)
            if saldo is None:
                return jsonify({"error": "Usuario no encontrado"}), 404

            if saldo < monto_apuesta:
                return jsonify({
                    "error": "Saldo insuficiente",
                    "saldo_actual": saldo,
                    "monto_apuesta": monto_apuesta
                }), 400

            # Débito previo al resultado (principio de prudencia)
            if not UserModel.update_balance(usuario_id, -monto_apuesta):
                return jsonify({"error": "No se pudo procesar la apuesta"}), 500

            import random
            ganó = random.random() > 0.6  # 40% probabilidad de ganar

            if ganó:
                premio = monto_apuesta * 2
                UserModel.update_balance(usuario_id, premio)  # devuelve apuesta + ganancia
                return jsonify({
                    "resultado": "GANADOR",
                    "premio": premio,
                    "nuevo_saldo": saldo - monto_apuesta + premio
                }), 200
            else:
                return jsonify({
                    "resultado": "PERDEDOR",
                    "mensaje": "Sigue intentando",
                    "nuevo_saldo": saldo - monto_apuesta
                }), 200

        except Exception as e:
            logger.error(f"Error procesando apuesta: {str(e)}")
            return jsonify({"error": "Error interno en el sistema de apuestas"}), 500