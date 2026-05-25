import mysql.connector
import random
from utils.database import get_db_connection, close_db_connection

class PollModel:
    @staticmethod
    def create_poll_group(nombre_grupo, creador_id):
        """Create a new poll group."""
        # Generate unique invitation code
        codigo_invitacion = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=6))

        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            sql = """INSERT INTO pollas_grupos (nombre_grupo, codigo_invitacion, creador_id)
                     VALUES (%s, %s, %s)"""
            cursor.execute(sql, (nombre_grupo, codigo_invitacion, creador_id))

            grupo_id = cursor.lastrowid
            conn.commit()
            cursor.close()
            close_db_connection(conn)

            return grupo_id, codigo_invitacion

        except mysql.connector.Error as err:
            raise Exception(f"Database error: {err.msg}")

    @staticmethod
    def get_all_poll_groups():
        """Get all poll groups."""
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)

            sql = "SELECT grupo_id, nombre_grupo, codigo_invitacion, creador_id FROM pollas_grupos ORDER BY grupo_id DESC"
            cursor.execute(sql)
            grupos = cursor.fetchall()

            cursor.close()
            close_db_connection(conn)

            return grupos

        except mysql.connector.Error as err:
            raise Exception(f"Database error: {err.msg}")

    @staticmethod
    def get_group_rankings(group_id):
        """Get rankings for a specific poll group."""
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)

            sql = """
            SELECT u.nombre, u.usuario_id, SUM(p.puntos_obtenidos) as puntos_totales,
                   COUNT(p.pronostico_id) as pronosticos_realizados
            FROM usuarios u
            LEFT JOIN pronosticos p ON u.usuario_id = p.usuario_id AND p.grupo_id = %s
            GROUP BY u.usuario_id, u.nombre
            ORDER BY puntos_totales DESC
            """

            cursor.execute(sql, (group_id,))
            ranking = cursor.fetchall()

            cursor.close()
            close_db_connection(conn)

            return ranking

        except mysql.connector.Error as err:
            raise Exception(f"Database error: {err.msg}")

    @staticmethod
    def join_poll_group(codigo_invitacion, usuario_id):
        """Join a user to a poll group using invitation code."""
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)

            # Find group by invitation code
            sql = "SELECT grupo_id FROM pollas_grupos WHERE codigo_invitacion = %s"
            cursor.execute(sql, (codigo_invitacion,))
            grupo = cursor.fetchone()

            if not grupo:
                cursor.close()
                close_db_connection(conn)
                return None

            # Add user to group
            sql = "INSERT INTO usuarios_pollas (usuario_id, grupo_id) VALUES (%s, %s)"
            cursor.execute(sql, (usuario_id, grupo['grupo_id']))

            conn.commit()
            cursor.close()
            close_db_connection(conn)

            return grupo['grupo_id']

        except mysql.connector.Error as err:
            raise Exception(f"Database error: {err.msg}")