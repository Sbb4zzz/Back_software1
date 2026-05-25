import mysql.connector
import random
from datetime import datetime, timedelta

# Configuración de la conexión
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'mundial_2026_hub',
    'port': 3307
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

def populate_sample_data():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Insertar partidos de muestra
        partidos = [
            ('Argentina', 'Brasil', '2026-06-15 16:00:00', 'Estadio Azteca', 'Ciudad de México', 'Fase de Grupos'),
            ('Francia', 'Alemania', '2026-06-16 20:00:00', 'Estadio Azteca', 'Ciudad de México', 'Fase de Grupos'),
            ('España', 'Inglaterra', '2026-06-17 16:00:00', 'Wembley', 'Londres', 'Fase de Grupos'),
            ('Portugal', 'Países Bajos', '2026-06-18 20:00:00', 'Johan Cruyff Arena', 'Ámsterdam', 'Fase de Grupos'),
            ('Argentina', 'Francia', '2026-06-25 16:00:00', 'Estadio Azteca', 'Ciudad de México', 'Cuartos de Final'),
        ]

        for partido in partidos:
            cursor.execute("""
                INSERT INTO partidos (equipo_a, equipo_b, fecha_hora, estadio, ciudad, fase)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, partido)

        # Insertar láminas de muestra
        laminas = [
  
        ]

        for lamina in laminas:
            cursor.execute("""
                INSERT INTO laminas (nombre_jugador, seleccion, rareza, imagen_url)
                VALUES (%s, %s, %s, %s)
            """, lamina)

        # Insertar entradas de muestra (10 por partido)
        cursor.execute("SELECT partido_id FROM partidos")
        partido_ids = [row[0] for row in cursor.fetchall()]

        for partido_id in partido_ids:
            for i in range(10):
                entrada_id = f"ENT-{partido_id}-{i+1:03d}"
                precio = round(random.uniform(50, 200), 2)
                cursor.execute("""
                    INSERT INTO entradas (entrada_id, partido_id, precio)
                    VALUES (%s, %s, %s)
                """, (entrada_id, partido_id, precio))

        conn.commit()
        cursor.close()
        conn.close()

        print("✅ Datos de muestra insertados exitosamente!")
        print(f"📅 {len(partidos)} partidos creados")
        print(f"🎴 {len(laminas)} láminas creadas")
        print(f"🎫 {len(partido_ids) * 10} entradas creadas")

    except mysql.connector.Error as err:
        print(f"❌ Error: {err}")

if __name__ == '__main__':
    populate_sample_data()