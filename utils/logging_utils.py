import logging
import uuid
from datetime import datetime
from utils.database import get_db_connection, close_db_connection

def log_evento(usuario_id, tipo_evento, descripcion, transaccion_id=None, datos_extra=None):
    """Log an audit event to the database."""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        sql = """INSERT INTO eventos_log
                 (usuario_id, tipo_evento, descripcion, transaccion_id, datos_extra, fecha_evento)
                 VALUES (%s, %s, %s, %s, %s, %s)"""

        cursor.execute(sql, (
            usuario_id,
            tipo_evento,
            descripcion,
            transaccion_id or str(uuid.uuid4()),
            str(datos_extra) if datos_extra else None,
            datetime.now()
        ))

        conn.commit()
        cursor.close()
        close_db_connection(conn)

    except Exception as e:
        logging.error(f"Error logging event: {str(e)}")