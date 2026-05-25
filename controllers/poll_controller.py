from flask import jsonify, request
from models.poll import PollModel
import logging

logger = logging.getLogger(__name__)

class PollController:
    @staticmethod
    def create_group():
        """Create a new poll group."""
        try:
            datos = request.get_json()
            nombre_grupo = datos.get('nombre_grupo')
            creador_id = datos.get('creador_id')

            if not nombre_grupo or not creador_id:
                return jsonify({"error": "Faltan datos obligatorios"}), 400

            grupo_id, codigo_invitacion = PollModel.create_poll_group(nombre_grupo, creador_id)

            # Log event (would need implementation)
            # log_evento(creador_id, 'crear_grupo', f'Creación de grupo de polla: {nombre_grupo}',
            #           str(uuid.uuid4()), {'grupo_id': grupo_id, 'codigo': codigo_invitacion})

            return jsonify({
                "mensaje": "Grupo creado exitosamente",
                "grupo_id": grupo_id,
                "codigo_invitacion": codigo_invitacion
            }), 201

        except Exception as e:
            logger.error(f"Error creando grupo: {str(e)}")
            return jsonify({"error": f"Error en el servidor: {str(e)}"}), 500

    @staticmethod
    def get_groups():
        """Get all poll groups."""
        try:
            grupos = PollModel.get_all_poll_groups()
            return jsonify({"groups": grupos}), 200

        except Exception as e:
            logger.error(f"Error obteniendo grupos: {str(e)}")
            return jsonify({"error": f"Error en el servidor: {str(e)}"}), 500

    @staticmethod
    def get_group_rankings(group_id):
        """Get rankings for a specific group."""
        try:
            ranking = PollModel.get_group_rankings(group_id)
            return jsonify({"ranking": ranking}), 200

        except Exception as e:
            logger.error(f"Error obteniendo ranking: {str(e)}")
            return jsonify({"error": f"Error en el servidor: {str(e)}"}), 500