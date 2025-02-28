#Importar as bibliotecas
from tkinter import * #Importa todos os modulos do tkinter
from tkinter import messagebox #Importa o modulo de caixas de mensagem do tkinter
from tkinter import ttk #Importa o modulo de widgets tematicos do tkinter
from DataBase import DataBase #Importa a classe database do modulo database

#CRIAR AS JANELAS

jan = Tk() #Cria uma instancia da janela principal
jan.title("SL Sytens - Painel de acesso") #Define o titulo da janela
jan.geometry("600x300") #Define o tamanho da janela 
jan.configure(background = "white") #Configura a cor de fundo da janela
jan.resizable(width = False, height = False) #Impede que a janela seja redimensionada

#Comando para deixar a tela transparente
jan.attributes("-alpha", 0.9) #Define a transparencia da janla (0.0 a 1.0)

#Define icone na janela
jan.iconbitmap(default = "icons/LogoIcon.ico") #Define o icone da janela

#Carregar imagem
logo = PhotoImage(file = "icons/LogoIsaac.png") #carrega imagem do logo

#Criar Frame 
LeftFrame = Frame(jan, width = 200, height = 300, bg = "MIDNIGHTBLUE", relief = "raise") #Cria o frame à esquerda
LeftFrame.pack(side = LEFT) #Posiciona o frame a esquerda

RightFrame = Frame(jan, width = 395, height = 300, bg = "MIDNIGHTBLUE", relief = "raise") #Cria o frame à direita
RightFrame.pack(side = RIGHT) #Posiciona o frame a direita

#Adicionar Logo
LogoLabel = Label(LeftFrame, image = logo, bg = "MIDNIGHTBLUE") #Cria um label para a imagem do logo
LogoLabel.place(x = 50, y = 100) #Posiciona o label no frame esquerdo

#Adicionar campos de usuario e senha
UsuarioLabel = Label(RightFrame, text = "Usuario: ", font = ("Century Gothic", 20), bg = "MIDNIGHTBLUE", fg = "White") #Cria um label para o usuario
UsuarioLabel.place(x = 5, y = 100) #Posiciona o label no frame direito
UsuarioEntry = ttk.Entry(RightFrame, width = 30) #Cria um campo de entrada para o usuario 
UsuarioEntry.place(x = 120, y = 115) #Posiciona o campo de entrada

SenhaLabel = Label(RightFrame, text = "Senha: ", font = ("Century Gothic", 20 ), bg = "MIDNIGHTBLUE", fg = "White") #Cria um label para senha
SenhaLabel.place(x = 5, y = 150) #Posiciona o label para o frame direito
SenhaEntry = ttk.Entry(RightFrame, width = 30, show = "•") #Cria um campo de entrada para a senha
SenhaEntry.place(x = 120, y = 165) #Posiciona o campo da entrada

#Função de login
def Login():
    usuario = UsuarioEntry.get() #Obtém o valor do campo de entrada do usuario
    senha = SenhaEntry.get() #Obtém o valor do campo de entrada da senha

    #Conectar ao banco de dados
    db = DataBase() #Cria uma instancia da classe DataBase
    db.cursor.execute("""SELECT * FROM usuario WHERE usuario = %s AND senha = %s""", (usuario, senha)) #Executa a consulta SQL para verificar o usuario e a senha
    VerifyLogin = db.cursor.fetchone() #Obtém o resultado da consulta

    #Verificar se o usuario foi encontrando 
    if VerifyLogin:
        messagebox.showinfo(title = "INFO LOGIN", message = "Acesso Confirmado, Bem Vindo!") #Exibe mensagem de sucesso
    else:
        messagebox.showinfo(title = "INFO LOGIN", message = "Acesso Negado. Verifique se esta cadastrado no sistema!") #Exibe mensagem de erro

#Criando Botões
LoginButton = ttk.Button(RightFrame, text = "LOGIN", width = 15, command = Login) #Cria um botão de login para fora da tela
LoginButton.place(x = 150, y = 225) #Posiciona o botão de login

#Função para registrar novo usuario
def Registrar():
    #Removendo botões de login
    LoginButton.place(x = 5000) #Move o botão de login para fora da tela
    RegisterButton.place(x = 5000) #Move o botão de registro para fora da tela

    #Inserindo widgets de cadastro 
    Nomelabel = Label(RightFrame, text = "Nome: ", font = ("Century Gothic", 20 ), bg = "MIDNIGHTBLUE", fg = "White") #Cria um label para nome
    Nomelabel.place(x = 5, y = 5) #Posiciona o label no frame direito 
    NomeEntry = ttk.Entry(RightFrame, width = 30) #Cria um campo de entrada para o nome
    NomeEntry.place(x = 120, y = 120) #Posiciona o campo de entrada