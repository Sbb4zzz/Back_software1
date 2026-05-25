import mysql.connector
from utils.database import get_db_connection, close_db_connection

class MatchModel:
    @staticmethod
    def get_all_matches():
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)

            sql = """SELECT * FROM partidos ORDER BY fecha_hora ASC"""
            cursor.execute(sql)
            partidos = cursor.fetchall()

            cursor.close()
            close_db_connection(conn)

            return partidos

        except mysql.connector.Error as err:
            raise Exception(f"Database error: {err.msg}")

    @staticmethod
    def get_match_by_id(match_id):
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)

            sql = "SELECT * FROM partidos WHERE partido_id = %s"
            cursor.execute(sql, (match_id,))
            partido = cursor.fetchone()

            cursor.close()
            close_db_connection(conn)

            return partido

        except mysql.connector.Error as err:
            raise Exception(f"Database error: {err.msg}")

    @staticmethod
    def update_match_status(match_id, status):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            sql = "UPDATE partidos SET estado = %s WHERE partido_id = %s"
            cursor.execute(sql, (status, match_id))

            conn.commit()
            cursor.close()
            close_db_connection(conn)

            return True

        except mysql.connector.Error as err:
            raise Exception(f"Database error: {err.msg}")

    @staticmethod
    def get_matches_by_phase(phase):
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)

            sql = "SELECT * FROM partidos WHERE fase = %s ORDER BY fecha_hora ASC"
            cursor.execute(sql, (phase,))
            partidos = cursor.fetchall()

            cursor.close()
            close_db_connection(conn)

            return partidos

        except mysql.connector.Error as err:
            raise Exception(f"Database error: {err.msg}")