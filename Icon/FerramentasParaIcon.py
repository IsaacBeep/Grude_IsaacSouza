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
jan.iconbitmap(default = "C:/Users/isaac_s_souza/Downloads/IS.png") #Define o icone da janela

#Carregar imagem
logo = PhotoImage(file = "C:/Users/isaac_s_souza/Downloads/IS.png") #carrega imagem do logo

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
    NomeLabel = Label(RightFrame, text = "Nome: ", font = ("Century Gothic", 20 ), bg = "MIDNIGHTBLUE", fg = "White") #Cria um label para nome
    NomeLabel.place(x = 5, y = 5) #Posiciona o label no frame direito 
    NomeEntry = ttk.Entry(RightFrame, width = 30) #Cria um campo de entrada para o nome
    NomeEntry.place(x = 120, y = 15) #Posiciona o campo de entrada

    EmailLabel = Label(RightFrame, text = "Email: ", font = ("Century Gothic", 20 ), bg = "MIDNIGHTBLUE", fg = "White") #Cria um label para o email
    EmailLabel.place(x = 5, y = 40) #Posiciona o label em um frame direito
    EmailEntry = ttk.Entry(RightFrame, width = 30) #Cria um campo de entrada para o email
    EmailEntry.place(x = 120, y = 55) #Posiciona o campo de entrada

#Função para registrar no banco de dados
    def RegistrarNoBanco():
        nome = NomeEntry.get() #Obtem o valor do campo de entrada do nome
        email = EmailEntry.get() #Obtem o valor do campo de entrada do email
        usuario = UsuarioEntry.get() #Obtem o valor do campo de entrada do usuario
        senha = SenhaEntry.get() #Obtem o valor do campo de entrada do senha

    #Verificar se todos os campos estão preenchidos
        if nome == "" or email == "" or usuario == "" or senha == "":
            messagebox.showerror(title = "Erro de Registro", message = "PREENCHA TODOS OS CAMPOS") #Exibe mensagem de erro
        else:
            db = DataBase() #Cria uma instancia de classe DataBase
            db.RegistrarNoBanco(nome, email, usuario, senha) #Chama o metodo para registrar no banco de dados
            messagebox.showinfo("Sucesso", "Usuario registrado com sucesso!") #Exibe mensagem de sucesso

            #Limpar os campos apos o registro
            NomeEntry.delete(0, END) #Limpa o campo de entrada do nome
            EmailEntry.delete(0, END) #Limpa o campo de entrada do email
            UsuarioEntry.delete(0, END) #Limpa o campo de entrada do usuario
            SenhaEntry.delete(0, END) #Limpa o campo de entrada da senha

    Register = ttk.Button(RightFrame, text = "REGISTRAR", width = 15, command = RegistrarNoBanco) #Cria um botão de registro
    Register.place(x = 150, y = 225) #Posiciona o botão de registro

#Função para voltar a tela de login
    def VoltarLogin():
    #Removendo widgets de cadastro
        NomeLabel.place(x = 5000) #Move o label do nome para fora da tela
        NomeEntry.place(x = 5000) #Move o campo de entrada do nome para fora da tela
        EmailLabel.place(x = 5000) #Move o label do email para fora da tela
        EmailEntry.place(x = 5000) #Move o campo de entrada email para fora da tela
        Register.place(x = 5000) #Move o botão de registro para fora da tela
        Voltar.place(x = 5000) #Move o botão de voltar para fora da tela

    #Trazendo de volta os widgets
    LoginButton.place(x = 150) #Traz o botão de registro de volta para a tela
    RegisterButton.place(x = 150) #Traz o botão de registrar de volta para a tela

    Voltar = ttk.Button(RightFrame, text = "VOLTAR", width = 15, command = VoltarLogin) #Cria um botão de voltar
    Voltar.place(x = 150, y = 255) #Posiciona o botão de registro
RegisterButton = ttk.Button(RightFrame, text = "REGISTRAR", width = 15, command = Registrar) #Cria um botão de registro
RegisterButton.place(x = 150, y = 255) #Posiciona o botão de registro

#Iniciar loop principal
jan.mainloop() #inicia o loop principal da aplicação



