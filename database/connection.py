# database/connection.py
import mysql.connector

def connect_to_db():
    try:
        cnx = mysql.connector.connect(
                host="localhost",
                port=3306,
                user="root",
                password="xxxxx", # Substitua pela senha do seu banco de dados
                database="mega"  # Substitua pelo nome do seu banco de dados
        )
        return cnx
    except mysql.connector.Error as err:
        print(f"Erro: {err}")
        return None
    
def create_database():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="xxxxxx" # Substitua pela senha do seu banco de dados
        )
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS mega")
        cursor.execute("USE mega")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tabela (
                id INT AUTO_INCREMENT PRIMARY KEY,
                coluna1 VARCHAR(255),
                coluna2 VARCHAR(255),
                coluna3 VARCHAR(255),
                coluna4 VARCHAR(255),
                coluna5 VARCHAR(255),
                coluna6 VARCHAR(255),
                coluna7 VARCHAR(255)
            )
        """)
        connection.commit()
        print("Banco de dados 'mega' e tabela 'tabela' criados com sucesso.")
    except mysql.connector.Error as err:
        print(f"Erro: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

create_database()