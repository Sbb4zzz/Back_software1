import mysql.connector

from utils.database import (
    get_db_connection,
    close_db_connection
)

conn = get_db_connection()
cursor = conn.cursor()

selecciones = [
    "Mexico",
    "Sudafrica",
    "Korea Del Sur",
    "Republica Checa",
    "Canada",
    "Bosnia y Herzegovina",
    "Qatar",
    "Suiza",
    "Brasil",
    "Marruecos",
    "Haiti",
    "Escocia",
    "EEUU",
    "Paraguay",
    "Australia",
    "Turquia",
    "Alemania",
    "Curazao",
    "Costa de Marfil",
    "Ecuador",
    "Paises Bajos",
    "Japon",
    "Suecia",
    "Tunez",
    "Belgica",
    "Egipto",
    "Iran",
    "Nueva Zelanda",
    "España",
    "Cabo Verde",
    "Arabia Saudita",
    "Uruguay",
    "Francia",
    "Senegal",
    "Irak",
    "Noruega",
    "Argentina",
    "Argelia",
    "Austria",
    "Jordania",
    "Portugal",
    "Congo",
    "Uzbekistan",
    "Colombia",
    "Inglaterra",
    "Croacia",
    "Ghana",
    "Panama"
]

# Limpiar tablas
cursor.execute("DELETE FROM coleccion_usuario")
cursor.execute("DELETE FROM laminas")

# Reiniciar IDs
cursor.execute("ALTER TABLE laminas AUTO_INCREMENT = 1")

# ESCUDOS
for seleccion in selecciones:

    sql = """
    INSERT INTO laminas (
        nombre_jugador,
        seleccion,
        posicion,
        especial,
        imagen_url
    )
    VALUES (%s, %s, %s, %s, %s)
    """

    valores = (
        f"Escudo {seleccion}",
        seleccion,
        "Escudo",
        False,
        f"{seleccion.lower().replace(' ', '_')}_escudo.png"
    )

    cursor.execute(sql, valores)

# JUGADORES
jugadores = {

    "Argentina": [
        ("Emiliano Martinez", "Arquero"),
        ("Cristian Romero", "Defensa"),
        ("Enzo Fernandez", "Mediocampista"),
        ("Lionel Messi", "Delantero"),
        ("Julian Alvarez", "Delantero")
    ],

    "Brasil": [
        ("Alisson", "Arquero"),
        ("Marquinhos", "Defensa"),
        ("Casemiro", "Mediocampista"),
        ("Vinicius Junior", "Delantero"),
        ("Rodrygo", "Delantero")
    ],

    "Colombia": [
        ("Camilo Vargas", "Arquero"),
        ("Davinson Sanchez", "Defensa"),
        ("Richard Rios", "Mediocampista"),
        ("Luis Diaz", "Delantero"),
        ("Jhon Duran", "Delantero")
    ],

    "Portugal": [
        ("Diogo Costa", "Arquero"),
        ("Ruben Dias", "Defensa"),
        ("Bernardo Silva", "Mediocampista"),
        ("Cristiano Ronaldo", "Delantero"),
        ("Rafael Leao", "Delantero")
    ]
}

for seleccion, lista_jugadores in jugadores.items():

    for jugador, posicion in lista_jugadores:

        sql = """
        INSERT INTO laminas (
            nombre_jugador,
            seleccion,
            posicion,
            especial,
            imagen_url
        )
        VALUES (%s, %s, %s, %s, %s)
        """

        valores = (
            jugador,
            seleccion,
            posicion,
            False,
            f"{jugador.lower().replace(' ', '_')}.png"
        )

        cursor.execute(sql, valores)

# ESPECIALES
especiales = [
    "Copa del Mundo",
    "Balon Oficial",
    "Mascota Mundial",
    "Logo WordlSync",
    "Logo Mundial",
    "Lionel Messi Extra",
    "Jeremy Doku Extra",
    "Vinicius Junior Extra",
    "Luis Diaz Extra",
    "Luka Modric Extra",
    "Lamine Yamal Extra",
    "Cristiano Ronaldo Extra",
    "Kylian Mbappe Extra",
    "Mohamed Salah Extra",
    "Erling Haaland Extra"
]

for especial in especiales:

    sql = """
    INSERT INTO laminas (
        nombre_jugador,
        seleccion,
        posicion,
        especial,
        imagen_url
    )
    VALUES (%s, %s, %s, %s, %s)
    """

    valores = (
        especial,
        "Especial",
        "Especial",
        True,
        f"{especial.lower().replace(' ', '_')}.png"
    )

    cursor.execute(sql, valores)

conn.commit()

cursor.close()
close_db_connection(conn)

print("Album cargado correctamente")