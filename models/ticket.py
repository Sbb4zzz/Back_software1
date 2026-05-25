import mysql.connector
from datetime import datetime, timedelta
from utils.database import get_db_connection, close_db_connection

class TicketModel:
    @staticmethod
    def get_available_tickets(match_id):
        """Get available tickets for a specific match."""
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)

            sql = """
            SELECT entrada_id, precio
            FROM entradas
            WHERE partido_id = %s AND estado = 'Disponible'
            ORDER BY entrada_id
            """

            cursor.execute(sql, (match_id,))
            entradas = cursor.fetchall()

            cursor.close()
            close_db_connection(conn)

            return entradas

        except mysql.connector.Error as err:
            raise Exception(f"Database error: {err.msg}")

    @staticmethod
    def reserve_ticket(ticket_id, user_id):
        """Reserve a ticket for a user."""
        reserva_expira = datetime.now() + timedelta(minutes=15)

        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            # Check if ticket is available
            cursor.execute("SELECT estado FROM entradas WHERE entrada_id = %s", (ticket_id,))
            result = cursor.fetchone()

            if not result or result[0] != 'Disponible':
                cursor.close()
                close_db_connection(conn)
                return False

            # Reserve the ticket
            sql = """
            UPDATE entradas
            SET estado = 'Reservada', usuario_id = %s, reserva_expira = %s
            WHERE entrada_id = %s AND estado = 'Disponible'
            """
            cursor.execute(sql, (user_id, reserva_expira, ticket_id))

            success = cursor.rowcount > 0
            conn.commit()
            cursor.close()
            close_db_connection(conn)

            return success

        except mysql.connector.Error as err:
            raise Exception(f"Database error: {err.msg}")

    @staticmethod
    def purchase_ticket(ticket_id, user_id):
        """Purchase a reserved ticket."""
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            # Check if ticket is reserved by this user and not expired
            cursor.execute("""
                SELECT estado, reserva_expira FROM entradas
                WHERE entrada_id = %s AND usuario_id = %s
            """, (ticket_id, user_id))
            result = cursor.fetchone()

            if not result or result[0] != 'Reservada':
                cursor.close()
                close_db_connection(conn)
                return False

            if result[1] and result[1] < datetime.now():
                # Reservation expired, release the ticket
                cursor.execute("UPDATE entradas SET estado = 'Disponible', usuario_id = NULL, reserva_expira = NULL WHERE entrada_id = %s", (ticket_id,))
                conn.commit()
                cursor.close()
                close_db_connection(conn)
                return False

            # Complete the purchase
            sql = "UPDATE entradas SET estado = 'Vendida' WHERE entrada_id = %s"
            cursor.execute(sql, (ticket_id,))

            conn.commit()
            cursor.close()
            close_db_connection(conn)

            return True

        except mysql.connector.Error as err:
            raise Exception(f"Database error: {err.msg}")

    @staticmethod
    def get_user_tickets(user_id):
        """Get all tickets purchased by a user."""
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)

            sql = """
            SELECT e.entrada_id, e.precio, e.estado, p.equipo_a, p.equipo_b, p.fecha_hora, p.estadio
            FROM entradas e
            JOIN partidos p ON e.partido_id = p.partido_id
            WHERE e.usuario_id = %s AND e.estado = 'Vendida'
            ORDER BY p.fecha_hora
            """

            cursor.execute(sql, (user_id,))
            entradas = cursor.fetchall()

            cursor.close()
            close_db_connection(conn)

            return entradas

        except mysql.connector.Error as err:
            raise Exception(f"Database error: {err.msg}")

    @staticmethod
    def cancel_reservation(ticket_id, user_id):
        """Cancel a ticket reservation."""
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            sql = """
            UPDATE entradas
            SET estado = 'Disponible', usuario_id = NULL, reserva_expira = NULL
            WHERE entrada_id = %s AND usuario_id = %s AND estado = 'Reservada'
            """
            cursor.execute(sql, (ticket_id, user_id))

            success = cursor.rowcount > 0
            conn.commit()
            cursor.close()
            close_db_connection(conn)

            return success

        except mysql.connector.Error as err:
            raise Exception(f"Database error: {err.msg}")