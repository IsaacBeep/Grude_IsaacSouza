import mysql.connector #Importa o módulo mysql.connector para conectar ao banco de dados MYSQL

class DataBase:
    def __init__(self):
        #Conecta ao banco de dados MySQL com as credenciais fornecidas
        self.conn = mysql.connector.connect(
            HOST = "localhost",
            USER = "root",
            PASSWORD = "",
            DATABASE = "IsaacSouza_db",
        )

        self.cursor = self.conn.cursor() #Cria um cursor para executar o comando SQL
        #Cria a tabela 'usuario' se ela não existir
        self.cursor.execute( '''CREATE TABLE IF NOT EXISTS 
        usuario
            (idUsuario INT AUTO_INCREMENT PRIMARY KEY,
            nome TEXT (255),
            email TEXT(255),
            usuario TEXT(255),
            senha TEXT (255),
            );''')
        
        self.conn.commit() #Confirma a criação da tabela 

        print("conectado ao banco de dados") #Imprime uma mensagem de confirmação

#Método para registrar um novo usuario no banco de dados
def RegistrarNoBanco(self, nome, email, usuario, senha):
    self.cursor.execute("INSERT INTO usuario (nome, email, usuario, senha) VALUES (%s, %s, %s, %s)", (nome, email, usuario, senha)) #Insere os dados na tabela
    self.conn.commit() #Confirma a inserção dos dados
    #Metódo para alterar os dados de um usuario existente no banco de dados
def alterar(self, idUsuario, nome, email, usuario, senha):
    self.cursor.execute("UPDATE usuario SET nome = %s, email = %s, usuario = %s, senha = %s WHERE idUsuario = %s", (nome, email, usuario, senha))
    self.conn.commit()

    #metodo para excluir um usuario do banco de dados
def excluir(self, idUsuario):
    self.cursor.execute("DELETE FROM usuario WHERE idUsuario = %s", (idUsuario,)) #Esclui o usuario no banco de dados com o id fornecido
    self.conn.commit()
    
    #metodo para buscar os dados de um usuario no banco de dados
def buscar(self, idUsuario):
    self.cursor.execute("SELECT * FROM usuario WHERE idUsuario = %s", (idUsuario,)) #Esclui o usuario no banco de dados com o id fornecido
    return self.cursor.fetchone()

    #metodo chamado quando a instancia da classe é destruida 
def __del__(self):
    self.conn.close() #Fecha a conexão com o banco de dados
        