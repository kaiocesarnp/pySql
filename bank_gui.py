#Produzir uma aplicação (um CRUD) de clientes em Python que pode receber e cadastrar um banco de clientes.
#CRUD, ou seja: ler, escrever, atualizar e apagar (Create, Read, Update e Delete)

#Importação do tkinter e definição do paddle
from tkinter import * #este módulo é utilizado sempre que temos que desenvolver uma interface gráfica

#class Gui(): #definimos uma classe chamada GUI ("Graphical User Interface”) fazendo referência a Interface Gráfica do Usuário
x_pad = 5 #x_pad e x_pad fazem referência a uma propriedade padding que estabelece o distanciamento entre o conteúdo de um elemento e a sua borda.
y_pad = 3
width_entry = 30 #A variável width_entry = 30 irá definir a largura da janela.

#Criando uma janela para a aplicação
window = Tk()
window.wm_title("PYSQL versão 1.0") #Nome fantasia da aplicação

# Definição das variáveis que recebem os dados inseridos pelo user
txtNome = StringVar()
txtSobrenome = StringVar()
txtEmail = StringVar()
txtCPF = StringVar()

#O argumento window é o que define a qual janela o Label deve pertencer.
lblnome = Label(window, text = "Nome")
lblsobrenome = Label(window, text = "Sobrenome")
lblemail = Label(window, text = "E-mail")
lblcpf = Label(window, text = "CPF")

# Campos de entrada
entNome = Entry(window, textvariable=txtNome, width=width_entry)
entSobrenome = Entry(window, textvariable=txtSobrenome, width=width_entry)
entEmail = Entry(window, textvariable=txtEmail, width=width_entry)
entCPF = Entry(window, textvariable=txtCPF, width=width_entry)

# Lista de clientes e scrollbar
listClientes = Listbox(window, width = 100)
scrollClientes = Scrollbar(window)

# Botões
btnViewAll = Button(window, text = "Ver todos")
btnBuscar = Button(window, text = "Buscar")
btnInserir = Button(window, text = "Inserir")
btnUpdate = Button(window, text = "Atualizar Selecionados")
btnDel = Button(window, text = "Deletar Selecionados")
btnClose = Button(window, text = "Fechar")

#Associar os objetos criados ao Grid da Janela
lblnome.grid(row=0, column = 0)
lblsobrenome.grid(row=1, column = 0)
lblemail.grid(row=2, column = 0)
lblcpf.grid(row=3, column = 0)

entNome.grid(row = 0, column = 1, padx = 50, pady = 50)
entSobrenome.grid(row = 1, column = 1)
entEmail.grid(row = 2, column = 1)
entCPF.grid(row = 3, column = 1)

listClientes.grid(row = 0, column = 2, rowspan = 10)
scrollClientes.grid(row = 0, column = 6, rowspan = 10)

btnViewAll.grid(row = 4, column = 0, columnspan = 2)
btnBuscar.grid(row = 5, column = 0, columnspan = 2)
btnInserir.grid(row = 6, column = 0, columnspan = 2)
btnUpdate.grid(row = 7, column = 0, columnspan = 2)
btnDel.grid(row = 8, column = 0, columnspan = 2)
btnClose.grid(row = 9, column = 0, columnspan = 2)

#Conectando o Scrollbar com a ListBox
listClientes.configure(yscrollcommand = scrollClientes.set)
scrollClientes.configure(command = listClientes.yview)

#Adicionando estilo (swag)
for child in window.winfo_children():
    widget_class = child.__class__.__name__
    if widget_class == "Button":
        child.grid_configure(sticky = 'WE', padx = x_pad, pady = y_pad)
    elif widget_class == "Listbox":
        child.grid_configure(padx = 0, pady = 0, sticky = 'NS')
    elif widget_class == "Scrollbar":
        child.grid_configure(padx = 0, pady = 0, sticky = 'NS')
    else:
        child.grid_configure (padx = x_pad, pady = y_pad, sticky = 'N')

#def run(self):
#    Gui.window.mainloop()

# Loop principal da aplicação
window.mainloop()
