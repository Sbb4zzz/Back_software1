from flask import jsonify, request
from models.user import UserModel
from utils.auth import generate_jwt_token, decode_jwt_token
import logging

logger = logging.getLogger(__name__)

class UserController:
    @staticmethod
    def register():
        """Handle user registration."""
        try:
            datos = request.get_json()

            print(datos)

            if not datos:
                return jsonify({"error": "No se recibió información"}), 400

            nombre = datos.get('nombre')
            email = datos.get('email')
            password = datos.get('password')
            rol = datos.get('rol', 'aficionado')

            if not nombre or not email or not password:
                return jsonify({"error": "Faltan campos obligatorios"}), 400

            if rol not in ['aficionado', 'operador', 'soporte']:
                return jsonify({"error": "Rol inválido"}), 400

            usuario = UserModel.create_user(nombre, email, password, rol)

            return jsonify({
                "usuario_id": usuario['usuario_id'],
                "nombre": usuario['nombre'],
                "email": usuario['email'],
                "rol": usuario['rol'],
                "puntos_totales": usuario['puntos_totales'],
                "created_at": usuario['created_at']
            }), 201

        except Exception as e:
            logger.error(f"Error en registro: {str(e)}")
            if 'Duplicate entry' in str(e):
                return jsonify({"error": "El email ya está registrado"}), 400
            return jsonify({"error": f"Error en el servidor: {str(e)}"}), 500

    @staticmethod
    def login():
        """Handle user login."""
        try:
            datos = request.get_json()
            email = datos.get('email')
            password = datos.get('password')

            if not email or not password:
                return jsonify({"error": "Faltan datos de acceso"}), 400

            usuario = UserModel.authenticate_user(email, password)

            if usuario:
                token = generate_jwt_token(usuario['usuario_id'], usuario['email'], usuario['rol'])

                return jsonify({
                    "token": token,
                    "access_token": token,
                    "user": {
                        "usuario_id": usuario['usuario_id'],
                        "nombre": usuario['nombre'],
                        "email": usuario['email'],
                        "rol": usuario['rol'],
                        "puntos_totales": usuario['puntos_totales']
                    }
                }), 200
            else:
                # Log failed login
                # log_evento(None, 'login_fallido', f'Intento de login fallido para email: {email}',
                #           str(uuid.uuid4()), {'email': email})
                return jsonify({"error": "Correo o contraseña incorrectos"}), 401

        except Exception as e:
            logger.error(f"Error en login: {str(e)}")
            return jsonify({"error": f"Error en el servidor: {str(e)}"}), 500

    @staticmethod
    def get_profile():
        """Get authenticated user profile."""
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Bearer '):
            return jsonify({"error": "Token no proporcionado"}), 401

        token = auth_header.split(' ', 1)[1]

        try:
            payload = decode_jwt_token(token)
            usuario = UserModel.get_user_by_id(payload['sub'])

            if not usuario:
                return jsonify({"error": "Usuario no encontrado"}), 404

            return jsonify({
                "usuario_id": usuario['usuario_id'],
                "nombre": usuario['nombre'],
                "email": usuario['email'],
                "rol": usuario['rol'],
                "puntos_totales": usuario['puntos_totales'],
                "favoriteTeams": [],
                "favoriteVenues": []
            }), 200

        except Exception as e:
            logger.error(f"Error en profile: {str(e)}")
            return jsonify({"error": str(e)}), 401

    @staticmethod
    def logout():
        """Handle user logout."""
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Bearer '):
            return jsonify({"error": "Token no proporcionado"}), 401

        token = auth_header.split(' ', 1)[1]

        try:
            decode_jwt_token(token)
            return jsonify({"message": "Sesión finalizada"}), 200
        except Exception as e:
            logger.error(f"Error en logout: {str(e)}")
            return jsonify({"error": str(e)}), 401