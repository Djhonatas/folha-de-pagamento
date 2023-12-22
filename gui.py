from tkinter import *
from tkinter import ttk, messagebox

#cores----------------------------------
cor_0 = "#595959"
cor_fundo_1 = "#EcE9E2"
cor_fundo_2 = "#595959"
cor_letra = "#403d3d"

#criando janela ------------------------

janela = Tk()
janela.title("")
janela.geometry('490x610')
janela.configure(background=cor_fundo_1)
janela.resizable(width=FALSE, height=FALSE)

# Frames

frameCima = Frame(janela, width=500, height=70, bg=cor_fundo_1, relief="flat")
frameCima.grid(row=0, column=0, columnspan=2, sticky=NSEW)

frameMeio = Frame(janela, width=500, height=300, bg=cor_fundo_1, relief="solid")
frameMeio.grid(row=1, column=0, sticky=NSEW)

frameMeio_H = Frame(frameMeio, width=500, height=50, bg=cor_fundo_1, relief="solid")
frameMeio_H.grid(row=0, column=0, sticky=NSEW)

frameMeio_B = Frame(frameMeio, width=500, height=200, bg=cor_fundo_1, relief="solid")
frameMeio_B.grid(row=1, column=0, sticky=NSEW)

frameBaixo = Frame(janela, width=500, height=150, bg=cor_fundo_1, relief="raised")
frameBaixo.grid(row=2, column=0,pady=10, sticky=NSEW)


#FRame Cima ---------------------------------------
app_logo = Label(frameCima, text= "Folha de Pagamento", compound=LEFT, padx=5, anchor=NW, font=('Arial, 22'), bg=cor_fundo_1, fg=cor_fundo_2)
app_logo.place(x=10, y=20)


#FRame meio ---------------------------------------
app_label = Label(frameMeio_H, text= "Dados do trabalhador", compound=LEFT, padx=5, anchor=NW, font=('Arial, 13'), bg=cor_fundo_1, fg=cor_0)
app_label.place(x=10, y=7)

app_linha = Label(frameMeio_H, width=270, anchor=NW, font=('Verdana 1'), bg=cor_0)
app_linha.place(x=190, y=17)
app_linha = Label(frameMeio_H, width=270, anchor=NW, font=('Verdana 1'), bg=cor_fundo_1)
app_linha.place(x=190, y=19)


l_nome = Label(frameMeio_B, text= "Nome*", anchor=NW, font=('Ivy 10'), bg=cor_fundo_1, fg=cor_letra)
l_nome.grid(row=0, column=0, padx=20, pady=5, sticky=NSEW)
e_nome = Entry(frameMeio_B, width=25, justify="left", relief=SOLID)
e_nome.grid(row=0, column=1, pady=5, sticky=NSEW)


l_cpf = Label(frameMeio_B, text="CPF*", anchor=NW, font=('Ivy', 10, 'bold'), bg=cor_fundo_1, fg=cor_letra)
l_cpf.grid(row=1, column=0, padx=20, pady=5, sticky=NSEW)
e_cpf = Entry(frameMeio_B, width=25, justify="left", relief=SOLID)
e_cpf.grid(row=1, column=1, pady=5, sticky=NSEW)


l_cargo = Label(frameMeio_B, text="Cargo*", anchor=NW, font=('Ivy', 10), bg=cor_fundo_1, fg=cor_letra)
l_cargo.grid(row=2, column=0, padx=20, pady=5, sticky=NSEW)
e_cargo = Entry(frameMeio_B, width=25, justify="left", relief=SOLID)
e_cargo.grid(row=2, column=1, pady=5, sticky=NSEW)


l_salario = Label(frameMeio_B, text="Salário Bruto*", anchor=NW, font=('Arial', 10), bg=cor_fundo_1, fg=cor_letra)
l_salario.grid(row=3, column=0, padx=20, pady=5, sticky=NSEW)
e_salario = Entry(frameMeio_B, width=25, justify="center", relief=SOLID)
e_salario.grid(row=3, column=1, pady=5, sticky=NSEW)

l_horas = Label(frameMeio_B, text="Horas Extras*", anchor=NW, font=('Arial', 10), bg=cor_fundo_1, fg=cor_letra)
l_horas.grid(row=3, column=2, padx=20, pady=5, sticky=NSEW)
e_horas = Entry(frameMeio_B, width=8, justify="center", relief=SOLID)
e_horas.grid(row=3, column=3, pady=5, sticky=NSEW)


#FRame Meio ---------------------------------------
app_logo = Label(frameBaixo, text= "Proventos", compound=LEFT, padx=5, anchor=NW, font=('Arial, 13'), bg=cor_fundo_1, fg=cor_fundo_2)
app_logo.place(x=10, y=7)


janela.mainloop()