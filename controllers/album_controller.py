from flask import jsonify, request
from models.album import AlbumModel
import logging

logger = logging.getLogger(__name__)

class AlbumController:
    @staticmethod
    def get_all_laminas():
        try:
            laminas = AlbumModel.get_all_laminas()
            return jsonify({"laminas": laminas}), 200

        except Exception as e:
            logger.error(f"Error obteniendo láminas: {str(e)}")
            return jsonify({"error": f"Error en el servidor: {str(e)}"}), 500

    @staticmethod
    def open_pack(user_id):
        try:

            resultado = AlbumModel.open_pack(user_id)

            if resultado.get("error"):

                return jsonify(resultado), 403

            return jsonify(resultado), 200

        except Exception as e:
            logger.error(f"Error abriendo paquete: {str(e)}")

            return jsonify({
                "error": f"Error en el servidor: {str(e)}"
            }), 500
        
    @staticmethod
    def get_collection():
        try:
            usuario_id = request.args.get('usuario_id')
            if not usuario_id:
                return jsonify({"error": "usuario_id requerido"}), 400

            coleccion = AlbumModel.get_user_collection(usuario_id)

            return jsonify({"coleccion": coleccion}), 200

        except Exception as e:
            logger.error(f"Error obteniendo colección: {str(e)}")
            return jsonify({"error": f"Error en el servidor: {str(e)}"}), 500

    @staticmethod
    def trade_cards():
        try:
            datos = request.get_json()
            usuario_origen = datos.get('usuario_origen')
            usuario_destino = datos.get('usuario_destino')
            lamina_origen = datos.get('lamina_origen')
            lamina_destino = datos.get('lamina_destino')

            if not all([usuario_origen, usuario_destino, lamina_origen, lamina_destino]):
                return jsonify({"error": "Faltan datos obligatorios"}), 400

            success = AlbumModel.trade_cards(usuario_origen, usuario_destino, lamina_origen, lamina_destino)

            if success:
                return jsonify({"mensaje": "Intercambio realizado exitosamente"}), 200
            else:
                return jsonify({"error": "No se pudo realizar el intercambio"}), 400

        except Exception as e:
            logger.error(f"Error en intercambio: {str(e)}")
            return jsonify({"error": f"Error en el servidor: {str(e)}"}), 500
        
    @staticmethod
    def get_selecciones():
        try:

            selecciones = AlbumModel.get_selecciones()

            return jsonify({
                "selecciones": selecciones
            }), 200

        except Exception as e:
            logger.error(f"Error obteniendo selecciones: {str(e)}")
            return jsonify({
                "error": f"Error en el servidor: {str(e)}"
            }), 500


    @staticmethod
    def get_album_seleccion(seleccion, user_id):
        try:

            album = AlbumModel.get_album_seleccion(
                seleccion,
                user_id
            )

            return jsonify({
                "seleccion": seleccion,
                "laminas": album
            }), 200

        except Exception as e:
            logger.error(f"Error obteniendo álbum: {str(e)}")
            return jsonify({
                "error": f"Error en el servidor: {str(e)}"
            }), 500


    @staticmethod
    def get_especiales(user_id):
        try:

            especiales = AlbumModel.get_especiales(
                user_id
            )

            return jsonify({
                "especiales": especiales
            }), 200

        except Exception as e:
            logger.error(f"Error obteniendo especiales: {str(e)}")
            return jsonify({
                "error": f"Error en el servidor: {str(e)}"
            }), 500


    @staticmethod
    def get_progreso(user_id):

        try:

            progreso = AlbumModel.get_progreso(
                user_id
            )

            return jsonify(progreso), 200

        except Exception as e:
            logger.error(f"Error obteniendo progreso: {str(e)}")
            return jsonify({
                "error": f"Error en el servidor: {str(e)}"
            }), 500