import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
import logging
from utils.database import get_db_connection, close_db_connection

logger = logging.getLogger(__name__)

class UserModel:

    @staticmethod
    def create_user(nombre, email, password, rol='aficionado'):
        """Crea un nuevo usuario en la base de datos con un ID único."""
        u_id = str(uuid.uuid4())
        pass_hashed = generate_password_hash(password)

        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)

            sql = """INSERT INTO usuarios
                     (usuario_id, nombre, email, password_hash, rol, saldo)
                     VALUES (%s, %s, %s, %s, %s, %s)"""
            cursor.execute(sql, (u_id, nombre, email, pass_hashed, rol, 0.00))
            conn.commit()

            cursor.execute("SELECT created_at FROM usuarios WHERE usuario_id = %s", (u_id,))
            result = cursor.fetchone()
            created_at = result['created_at'].isoformat() if result and result.get('created_at') else None

            cursor.close()
            close_db_connection(conn)

            return {
                'usuario_id': u_id,
                'nombre': nombre,
                'email': email,
                'rol': rol,
                'puntos_totales': 0,
                'saldo': 0.00,
                'created_at': created_at
            }

        except mysql.connector.Error as err:
            raise Exception(f"Error de base de datos: {err.msg}")

    @staticmethod
    def authenticate_user(email, password):
        """Autentica por email y retorna solo campos públicos (sin password_hash)."""
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)

            # ✅ SELECT explícito para no exponer password_hash
            sql = """SELECT usuario_id, nombre, email, rol, puntos_totales, saldo, created_at
                     FROM usuarios WHERE email = %s"""
            cursor.execute(sql, (email,))
            usuario = cursor.fetchone()

            # Verificar password por separado
            cursor.execute("SELECT password_hash FROM usuarios WHERE email = %s", (email,))
            hash_row = cursor.fetchone()

            cursor.close()
            close_db_connection(conn)

            if usuario and hash_row and check_password_hash(hash_row['password_hash'], password):
                # Serializar saldo y fechas
                if usuario.get('saldo') is not None:
                    usuario['saldo'] = float(usuario['saldo'])
                if usuario.get('created_at') and hasattr(usuario['created_at'], 'isoformat'):
                    usuario['created_at'] = usuario['created_at'].isoformat()
                return usuario

            return None

        except mysql.connector.Error as err:
            raise Exception(f"Error de base de datos: {err.msg}")

    @staticmethod
    def get_user_by_id(user_id):
        """Obtiene la información pública de un usuario por su ID."""
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)

            sql = """SELECT usuario_id, nombre, email, rol, puntos_totales, saldo, created_at
                     FROM usuarios WHERE usuario_id = %s"""
            cursor.execute(sql, (user_id,))
            usuario = cursor.fetchone()

            cursor.close()
            close_db_connection(conn)

            if not usuario:
                return None

            # ✅ Serializar tipos no-JSON
            usuario['saldo'] = float(usuario['saldo']) if usuario.get('saldo') is not None else 0.0
            if usuario.get('created_at') and hasattr(usuario['created_at'], 'isoformat'):
                usuario['created_at'] = usuario['created_at'].isoformat()

            return usuario

        except mysql.connector.Error as err:
            raise Exception(f"Error de base de datos: {err.msg}")

    @staticmethod
    def get_user_balance(usuario_id):
        """
        Obtiene el saldo actual por usuario_id.
        Retorna float si existe, None si el usuario no existe.
        """
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)

            # ✅ Solo por ID (más seguro y predecible)
            cursor.execute(
                "SELECT saldo FROM usuarios WHERE usuario_id = %s",
                (usuario_id,)
            )
            result = cursor.fetchone()

            cursor.close()
            close_db_connection(conn)

            if result is None:
                logger.warning(f"get_user_balance: usuario {usuario_id} no encontrado")
                return None  # ✅ None != saldo 0, el controller puede distinguirlos

            return float(result['saldo'])

        except mysql.connector.Error as err:
            raise Exception(f"Error al obtener saldo: {err.msg}")

    @staticmethod
    def update_balance(usuario_id, monto):
        """
        Actualiza el saldo del usuario de forma atómica.
        - monto positivo → crédito
        - monto negativo → débito
        Retorna True si se actualizó, False si no hay saldo suficiente o no existe el usuario.
        """
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            # ✅ Protección atómica contra saldo negativo en la misma query
            sql = """
                UPDATE usuarios
                SET saldo = saldo + %s
                WHERE usuario_id = %s
                  AND (saldo + %s) >= 0
            """
            cursor.execute(sql, (monto, usuario_id, monto))
            conn.commit()

            filas_afectadas = cursor.rowcount
            cursor.close()
            close_db_connection(conn)

            if filas_afectadas == 0:
                logger.warning(
                    f"update_balance fallido | usuario={usuario_id} delta={monto} "
                    f"(saldo insuficiente o usuario no existe)"
                )
                return False

            return True

        except mysql.connector.Error as err:
            raise Exception(f"Error al actualizar saldo: {err.msg}")

    @staticmethod
    def update_user_points(user_id, points):
        """Actualiza los puntos totales acumulados por el usuario."""
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            sql = "UPDATE usuarios SET puntos_totales = puntos_totales + %s WHERE usuario_id = %s"
            cursor.execute(sql, (points, user_id))

            conn.commit()
            cursor.close()
            close_db_connection(conn)

            return True

        except mysql.connector.Error as err:
            raise Exception(f"Error de base de datos: {err.msg}")