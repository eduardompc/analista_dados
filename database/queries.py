# database/queries.py
from .connection import connect_to_db

def insert_data(data):
    cnx = connect_to_db()
    if cnx:
        cursor = cnx.cursor()
        # ... (consulta SQL para inserir dados)
        cnx.commit()
        cursor.close()
        cnx.close()