from flask import jsonify, request
from models.ticket import TicketModel
import logging

logger = logging.getLogger(__name__)

class TicketController:
    @staticmethod
    def get_available_tickets(match_id):
        """Get available tickets for a match."""
        try:
            entradas = TicketModel.get_available_tickets(match_id)
            return jsonify({"entradas_disponibles": entradas}), 200

        except Exception as e:
            logger.error(f"Error obteniendo entradas: {str(e)}")
            return jsonify({"error": f"Error en el servidor: {str(e)}"}), 500

    @staticmethod
    def reserve_ticket():
        """Reserve a ticket."""
        try:
            datos = request.get_json()
            entrada_id = datos.get('entrada_id')
            usuario_id = datos.get('usuario_id')

            if not entrada_id or not usuario_id:
                return jsonify({"error": "Faltan datos obligatorios"}), 400

            success = TicketModel.reserve_ticket(entrada_id, usuario_id)

            if success:
                return jsonify({"mensaje": "Entrada reservada exitosamente"}), 200
            else:
                return jsonify({"error": "Entrada no disponible"}), 400

        except Exception as e:
            logger.error(f"Error reservando entrada: {str(e)}")
            return jsonify({"error": f"Error en el servidor: {str(e)}"}), 500

    @staticmethod
    def purchase_ticket():
        """Purchase a reserved ticket."""
        try:
            datos = request.get_json()
            entrada_id = datos.get('entrada_id')
            usuario_id = datos.get('usuario_id')

            if not entrada_id or not usuario_id:
                return jsonify({"error": "Faltan datos obligatorios"}), 400

            success = TicketModel.purchase_ticket(entrada_id, usuario_id)

            if success:
                return jsonify({"mensaje": "Compra realizada exitosamente"}), 200
            else:
                return jsonify({"error": "No se pudo completar la compra"}), 400

        except Exception as e:
            logger.error(f"Error comprando entrada: {str(e)}")
            return jsonify({"error": f"Error en el servidor: {str(e)}"}), 500

    @staticmethod
    def get_user_tickets(user_id):
        """Get user's purchased tickets."""
        try:
            entradas = TicketModel.get_user_tickets(user_id)
            return jsonify({"entradas": entradas}), 200

        except Exception as e:
            logger.error(f"Error obteniendo entradas del usuario: {str(e)}")
            return jsonify({"error": f"Error en el servidor: {str(e)}"}), 500