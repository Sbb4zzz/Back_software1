import mysql.connector
import random

from datetime import datetime, timedelta

from utils.database import (
    get_db_connection,
    close_db_connection
)
class AlbumModel:

    @staticmethod
    def get_all_laminas():

        try:

            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)

            sql = """
            SELECT
                lamina_id,
                nombre_jugador,
                seleccion,
                posicion,
                especial,
                imagen_url
            FROM laminas
            ORDER BY seleccion, nombre_jugador
            """

            cursor.execute(sql)

            laminas = cursor.fetchall()

            cursor.close()
            close_db_connection(conn)

            return laminas

        except mysql.connector.Error as err:
            raise Exception(f"Database error: {err.msg}")

    @staticmethod
    def open_pack(user_id):

        PRECIO_SOBRE = 3500

        try:

            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)

            # =========================
            # VERIFICAR USUARIO Y SALDO
            # =========================

            cursor.execute("""
                SELECT saldo
                FROM usuarios
                WHERE usuario_id = %s
            """, (user_id,))

            usuario = cursor.fetchone()

            if not usuario:

                cursor.close()
                close_db_connection(conn)

                return {
                    "error": "Usuario no encontrado"
                }

            saldo_actual = float(usuario['saldo'])

            if saldo_actual < PRECIO_SOBRE:

                cursor.close()
                close_db_connection(conn)

                return {
                    "error": "Saldo insuficiente",
                    "saldo_actual": saldo_actual,
                    "precio_sobre": PRECIO_SOBRE
                }

            # =========================
            # CONTROL DIARIO SOBRES
            # =========================

            cursor.execute("""
                SELECT *
                FROM control_sobres
                WHERE usuario_id = %s
            """, (user_id,))

            control = cursor.fetchone()

            hoy = datetime.now().date()

            # Crear registro si no existe
            if not control:

                cursor.execute("""
                    INSERT INTO control_sobres
                    (
                        usuario_id,
                        sobres_abiertos,
                        ultima_apertura
                    )
                    VALUES (%s, %s, %s)
                """, (
                    user_id,
                    0,
                    hoy
                ))

                conn.commit()

                cursor.execute("""
                    SELECT *
                    FROM control_sobres
                    WHERE usuario_id = %s
                """, (user_id,))

                control = cursor.fetchone()

            sobres_abiertos = control['sobres_abiertos']
            ultima_apertura = control['ultima_apertura']

            # =========================
            # REINICIAR SI ES OTRO DIA
            # =========================

            if ultima_apertura != hoy:

                sobres_abiertos = 0

                cursor.execute("""
                    UPDATE control_sobres
                    SET sobres_abiertos = 0,
                    ultima_apertura = %s
                    WHERE usuario_id = %s
                """, (
                    hoy,
                    user_id
                ))

                conn.commit()

            # =========================
            # VALIDAR LIMITE DIARIO
            # =========================

            if sobres_abiertos >= 4:

                cursor.close()
                close_db_connection(conn)

                return {
                    "error": "Limite diario alcanzado",
                    "sobres_restantes": 0
                }

            # =========================
            # DESCONTAR SALDO
            # =========================

            nuevo_saldo = saldo_actual - PRECIO_SOBRE

            cursor.execute("""
                UPDATE usuarios
                SET saldo = %s
                WHERE usuario_id = %s
            """, (
                nuevo_saldo,
                user_id
            ))

            # =========================
            # OBTENER LAMINAS
            # =========================

            cursor.execute("""
                SELECT
                    lamina_id,
                    nombre_jugador,
                    seleccion,
                    posicion,
                    especial,
                    imagen_url
                FROM laminas
            """)

            laminas_disponibles = cursor.fetchall()

            if not laminas_disponibles:

                cursor.close()
                close_db_connection(conn)

                return {
                    "error": "No hay laminas disponibles"
                }

            # =========================
            # PESOS DE RAREZA
            # =========================

            pesos = []

            for lamina in laminas_disponibles:

                if lamina['especial']:
                    pesos.append(15)

                else:
                    pesos.append(85)

            # =========================
            # ABRIR SOBRE
            # =========================

            laminas_obtenidas = random.choices(
                laminas_disponibles,
                weights=pesos,
                k=5
            )

            # =========================
            # GUARDAR EN COLECCION
            # =========================

            for lamina in laminas_obtenidas:

                cursor.execute("""
                    INSERT INTO coleccion_usuario
                    (
                        usuario_id,
                        lamina_id,
                        cantidad
                    )
                    VALUES (%s, %s, 1)

                    ON DUPLICATE KEY UPDATE
                    cantidad = cantidad + 1
                """, (
                    user_id,
                    lamina['lamina_id']
            ))

            # =========================
            # ACTUALIZAR CONTROL
            # =========================

            sobres_abiertos += 1

            cursor.execute("""
                UPDATE control_sobres
                SET sobres_abiertos = %s,
                    ultima_apertura = %s
                WHERE usuario_id = %s
            """, (
                sobres_abiertos,
                hoy,
                user_id
            ))

            conn.commit()

            cursor.close()
            close_db_connection(conn)

            return {
                "mensaje": "Sobre abierto exitosamente",
                "saldo_restante": nuevo_saldo,
                "sobres_restantes": 4 - sobres_abiertos,
                "laminas": laminas_obtenidas
            }

        except mysql.connector.Error as err:

            raise Exception(f"Database error: {err.msg}")

    @staticmethod
    def get_user_collection(user_id):

        try:

            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)

            sql = """
            SELECT
                l.lamina_id,
                l.nombre_jugador,
                l.seleccion,
                l.posicion,
                l.especial,
                l.imagen_url,
                c.cantidad

            FROM coleccion_usuario c

            INNER JOIN laminas l
                ON l.lamina_id = c.lamina_id

            WHERE c.usuario_id = %s

            ORDER BY l.seleccion, l.nombre_jugador
            """

            cursor.execute(sql, (user_id,))

            coleccion = cursor.fetchall()

            cursor.close()
            close_db_connection(conn)

            return coleccion

        except mysql.connector.Error as err:
            raise Exception(f"Database error: {err.msg}")

    @staticmethod
    def get_selecciones():

        try:

            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)

            cursor.execute("""
                SELECT DISTINCT seleccion
                FROM laminas
                WHERE seleccion != 'Especial'
                ORDER BY seleccion
            """)

            selecciones = cursor.fetchall()

            cursor.close()
            close_db_connection(conn)

            return selecciones

        except mysql.connector.Error as err:
            raise Exception(f"Database error: {err.msg}")

    @staticmethod
    def get_album_seleccion(seleccion, user_id):

        try:

            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)

            sql = """
            SELECT
                l.lamina_id,
                l.nombre_jugador,
                l.posicion,
                l.imagen_url,
                COALESCE(c.cantidad, 0) as cantidad

            FROM laminas l

            LEFT JOIN coleccion_usuario c
                ON l.lamina_id = c.lamina_id
                AND c.usuario_id = %s

            WHERE l.seleccion = %s

            ORDER BY l.posicion
            """

            cursor.execute(sql, (
                user_id,
                seleccion
            ))

            album = cursor.fetchall()

            cursor.close()
            close_db_connection(conn)

            return album

        except mysql.connector.Error as err:
            raise Exception(f"Database error: {err.msg}")

    @staticmethod
    def get_especiales(user_id):

        try:

            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)

            sql = """
            SELECT
                l.lamina_id,
                l.nombre_jugador,
                l.imagen_url,
                COALESCE(c.cantidad, 0) as cantidad

            FROM laminas l

            LEFT JOIN coleccion_usuario c
                ON l.lamina_id = c.lamina_id
                AND c.usuario_id = %s

            WHERE l.especial = TRUE
            """

            cursor.execute(sql, (user_id,))

            especiales = cursor.fetchall()

            cursor.close()
            close_db_connection(conn)

            return especiales

        except mysql.connector.Error as err:
            raise Exception(f"Database error: {err.msg}")

    @staticmethod
    def get_progreso(user_id):

        try:

            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)

            cursor.execute("""
                SELECT COUNT(*) as total
                FROM laminas
            """)

            total = cursor.fetchone()['total']

            cursor.execute("""
                SELECT COUNT(*) as obtenidas
                FROM coleccion_usuario
                WHERE usuario_id = %s
            """, (user_id,))

            obtenidas = cursor.fetchone()['obtenidas']

            porcentaje = round(
                (obtenidas / total) * 100,
                2
            )

            cursor.close()
            close_db_connection(conn)

            return {
                "total_laminas": total,
                "obtenidas": obtenidas,
                "progreso": porcentaje
            }

        except mysql.connector.Error as err:
            raise Exception(f"Database error: {err.msg}")

    @staticmethod
    def trade_cards(
        user_origin,
        user_destino,
        card_origin,
        card_destino
    ):

        try:

            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("""
                SELECT COUNT(*)
                FROM coleccion_usuario
                WHERE usuario_id = %s
                AND lamina_id = %s
                AND cantidad > 0
            """, (
                user_origin,
                card_origin
            ))

            origin_has_card = cursor.fetchone()[0] > 0

            cursor.execute("""
                SELECT COUNT(*)
                FROM coleccion_usuario
                WHERE usuario_id = %s
                AND lamina_id = %s
                AND cantidad > 0
            """, (
                user_destino,
                card_destino
            ))

            destino_has_card = cursor.fetchone()[0] > 0

            if not origin_has_card or not destino_has_card:

                cursor.close()
                close_db_connection(conn)

                return False

            # Intercambio
            cursor.execute("""
                UPDATE coleccion_usuario
                SET cantidad = cantidad - 1
                WHERE usuario_id = %s
                AND lamina_id = %s
            """, (
                user_origin,
                card_origin
            ))

            cursor.execute("""
                INSERT INTO coleccion_usuario (
                    usuario_id,
                    lamina_id,
                    cantidad
                )
                VALUES (%s, %s, 1)
                ON DUPLICATE KEY UPDATE
                cantidad = cantidad + 1
            """, (
                user_destino,
                card_origin
            ))

            cursor.execute("""
                UPDATE coleccion_usuario
                SET cantidad = cantidad - 1
                WHERE usuario_id = %s
                AND lamina_id = %s
            """, (
                user_destino,
                card_destino
            ))

            cursor.execute("""
                INSERT INTO coleccion_usuario (
                    usuario_id,
                    lamina_id,
                    cantidad
                )
                VALUES (%s, %s, 1)
                ON DUPLICATE KEY UPDATE
                cantidad = cantidad + 1
            """, (
                user_origin,
                card_destino
            ))

            conn.commit()

            cursor.close()
            close_db_connection(conn)

            return True

        except mysql.connector.Error as err:
            raise Exception(f"Database error: {err.msg}")