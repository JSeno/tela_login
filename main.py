# TODO: Alterar o sitema de usuário colocando um dicionário e buscando pela key e value deles para fazer o login.

#-- Importando Tkinter
from tkinter import *
from tkinter import ttk, Tk  # Importando ttk, que é uma biblioteca para criar widgets
from tkinter import messagebox  # Essa biblioteca é para aparecer uma janela de alerta

#-- Paleta de Cores
cor0 = "#f0f3f5"  # Preta / black
cor1 = "#feffff"  # branca / white
cor2 = "#3fb5a3"  # verde / green
cor3 = "#38576b"  # valor / value
cor4 = "#403d3d"   # letra / letters

#-- Criando a janela
janela = Tk()
janela.title('')
janela.geometry('310x300')
janela.configure(background=cor1)
janela.resizable(False, False)

#-- Dividindo a janela com os frames
frame_cima = Frame(janela, width=310, height=50, bg=cor1, relief=FLAT)
frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frame_baixo = Frame(janela, width=310, height=250, bg=cor1, relief=FLAT)
frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

#-- Configurando o frame_cima
l_nome = Label(frame_cima, text='LOGIN', anchor=NE, font=('Ivy 25'), bg=cor1, fg=cor4)
l_nome.place(x=5, y=5)

l_linha = Label(frame_cima, text='', width=275, height=1, anchor=NW, font=('Ivy 1'), bg=cor2)
l_linha.place(x=10, y=45)

#-- Parte lógica do programa
credenciais = ['joao', '123456']

def verifica_senha():
    nome = e_nome.get()
    senha = e_pass.get()

    if nome == 'admin' and senha == 'admin':
        messagebox.showinfo('Login', 'Login efetuado com sucesso!')
        
    elif credenciais[0] == nome and credenciais[1] == senha:
        messagebox.showinfo('Login', 'Login efetuado com sucesso!' + ' ' + credenciais[0] )

        # Apagar os campos nos frame_cima e frame_baixo
        for widget in frame_baixo.winfo_children():
            widget.destroy()

        for widget in frame_cima.winfo_children():
            widget.destroy()

        nova_janela()

    else:
        messagebox.showwarning('Login', 'Login ou senha incorretos!')
        janela.destroy()

#-- Essa função altera a tela do login mostrando no nome do usuário    
def nova_janela():
    l_nome = Label(frame_cima, text='Usuário: ' + credenciais[0], anchor=NE, font=('Ivy 20'), bg=cor1, fg=cor4)
    l_nome.place(x=5, y=5)

    l_linha = Label(frame_cima, text='', width=275, height=1, anchor=NW, font=('Ivy 1'), bg=cor2)
    l_linha.place(x=10, y=45)

    l_nome = Label(frame_baixo, text='Seja bem-vindo' + ' ' + credenciais[0], anchor=NE, font=('Ivy 20'), bg=cor1, fg=cor4)
    l_nome.place(x=5, y=105)


#-- Configurando o frame_baixo
l_nome = Label(frame_baixo, text='Nome *', anchor=NW, font=('Ivy 10'), bg=cor1, fg=cor4)
l_nome.place(x=10, y=20)

e_nome = Entry(frame_baixo, width=25, justify=LEFT, font=('', 15), highlightthickness=1, relief=SOLID)
e_nome.place(x=10, y=50)

l_pass = Label(frame_baixo, text='Password *', anchor=NW, font=('Ivy 10'), bg=cor1, fg=cor4)
l_pass.place(x=10, y=95)

e_pass = Entry(frame_baixo, width=25, justify=LEFT, show='*', font=('', 15), highlightthickness=1, relief=SOLID)
e_pass.place(x=10, y=125)

b_confirmar = Button(frame_baixo, command=verifica_senha, text='Entrar', width=39, height=2, font=('Ivy 8'), bg=cor2, fg=cor1, relief=RAISED, anchor=CENTER, overrelief=RIDGE)
b_confirmar.place(x=35, y=180)

#-- mainloop serve para que a janela fique em loop
janela.mainloop()
