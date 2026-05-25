import mysql.connector
from config import Config

def get_db_connection():
    """Establishes and returns a database connection."""
    try:
        conn = mysql.connector.connect(**Config.DB_CONFIG)
        return conn
    except mysql.connector.Error as err:
        print(f"Database connection error: {err}")
        raise

def close_db_connection(conn):
    """Closes the database connection."""
    if conn:
        conn.close()