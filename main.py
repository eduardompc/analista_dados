# main.py

import sys
from PyQt5.QtWidgets import QApplication

from interface.main_window import MainWindow  # Importe a classe MainWindow
from database.connection import connect_to_db


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Conecte ao banco de dados
    import mysql.connector

    def connect_to_db():
        try:
            connection = mysql.connector.connect(
                host="localhost",
                port=3306,
                user="root",
                password="xxxxxx", # Substitua pela senha do seu banco de dados
                database="mega"  # Substitua pelo nome do seu banco de dados
            )
            def create_database():
                try:
                    connection = mysql.connector.connect(
                        host="localhost",
                        port=3306,
                        user="root",
                        password="xxxxx" # Substitua pela senha do seu banco de dados
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
            if connection.is_connected():
                print("Conexão ao banco de dados MySQL foi bem-sucedida.")
                return connection
        except mysql.connector.Error as err:
            print(f"Erro: {err}")
            return None
    
    if not connect_to_db():
        print("Erro ao conectar ao banco de dados. Encerrando a aplicação.")
        sys.exit(1)  # Encerra a aplicação se a conexão falhar

    window = MainWindow()
    window.show()

    # Exemplo de como chamar uma função de análise (ajuste conforme necessário)
    # dados = window.obter_dados_da_tabela()  # Supondo que MainWindow tenha um método para obter os dados
    # resultado_regressao = realizar_regressao_linear(dados)
    # window.exibir_resultados(resultado_regressao)  # Supondo que MainWindow tenha um método para exibir os resultados

    sys.exit(app.exec_())