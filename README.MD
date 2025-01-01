# Projeto de Análise de Dados com Interface Gráfica

Este projeto consiste em uma aplicação com interface gráfica para análise de dados utilizando Python, PyQt, MySQL, Pandas e outras bibliotecas.

## Funcionalidades

* Importar dados de arquivos Excel.
* Realizar análises estatísticas e de Machine Learning.
* Visualizar os resultados das análises na interface gráfica.
* Salvar os dados e resultados no banco de dados MySQL.
* API RESTful para acesso aos dados e análises (documentação Swagger em /apidocs).

## Tecnologias Utilizadas

* Python 3.7+
* PyQt5
* MySQL
* Pandas
* NumPy
* Scikit-learn
* Statsmodels
* Flask
* Flasgger

## Instalação

1. Clone o repositório: `git clone https://github.com/eduardompc/analista_dados.git`
2. Crie um ambiente virtual: `python3 -m venv .venv`
3. Ative o ambiente virtual: `source .venv/bin/activate`
4. Instale as dependências: `pip install -r requirements.txt`
5. Configure o banco de dados MySQL:
    * Crie um banco de dados no MySQL.
    * Atualize as credenciais de acesso em `database/connection.py`.
6. Execute as migrations do banco de dados (se aplicável): `python manage.py migrate`

## Como Usar

1. Execute a aplicação: `python main.py`
2. Importe o arquivo de dados através da interface gráfica.
3. Selecione o tipo de análise e os parâmetros desejados.
4. Execute a análise e visualize os resultados.
5. Acesse a documentação da API em: `http://localhost:5000/apidocs`

## Contribuição

Sinta-se à vontade para contribuir com o projeto!

## Licença

MIT License

## Autor

EDUARDO CARVALHO

## Contato

eduardomarciopc@gmail.com