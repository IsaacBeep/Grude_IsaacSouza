# orientações para criar o banco 
# pip install mysql-connector-python <-- RODAR esse comando no console do python
# lembrar de instalar o connector do mysql
# criar o banco de dados no Mysql 


import mysql.connector

class Banco():
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="testesergio_db"
        )
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS usuario (
                     idUsuario INT AUTO_INCREMENT PRIMARY KEY,
                     nome VARCHAR(255),
                     telefone VARCHAR(255),
                     email VARCHAR(255),
                     usuario VARCHAR(255),
                     senha VARCHAR(255))""")
        self.conexao.commit()
        c.close()
