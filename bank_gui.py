#Produzir uma aplicação (um CRUD) de clientes em Python que pode receber e cadastrar um banco de clientes.
#CRUD, ou seja: ler, escrever, atualizar e apagar (Create, Read, Update e Delete)

#Importação do tkinter e definição do paddle
from tkinter import * #este módulo é utilizado sempre que temos que desenvolver uma interface gráfica

class Gui(): #definimos uma classe chamada GUI ("Graphical User Interface”) fazendo referência a Interface Gráfica do Usuário
    x_pad = 5 #x_pad e x_pad fazem referência a uma propriedade padding que estabelece o distanciamento entre o conteúdo de um elemento e a sua borda.
    y_pad = 3
    width_entry = 30 #A variável width_entry = 30 irá definir a largura da janela.

#Criando uma janela para a aplicação
    def __init__(self):
        self.window = Tk()
        self.window.wm_title("PYSQL versão 1.0")

# Definição das variáveis que recebem os dados inseridos pelo usuário
        self.txtNome = StringVar()
        self.txtSobrenome = StringVar()
        self.txtEmail = StringVar()
        self.txtCPF = StringVar()

#O argumento window é o que define a qual janela o Label deve pertencer.
        self.lblnome = Label(self.window, text="Nome")
        self.lblsobrenome = Label(self.window, text="Sobrenome")
        self.lblemail = Label(self.window, text="E-mail")
        self.lblcpf = Label(self.window, text="CPF")
        
# Campos de entrada
        self.entNome = Entry(self.window, textvariable=self.txtNome, width=self.width_entry)
        self.entSobrenome = Entry(self.window, textvariable=self.txtSobrenome, width=self.width_entry)
        self.entEmail = Entry(self.window, textvariable=self.txtEmail, width=self.width_entry)
        self.entCPF = Entry(self.window, textvariable=self.txtCPF, width=self.width_entry)

# Lista de clientes e scrollbar
        self.listClientes = Listbox(self.window, width=100)
        self.scrollClientes = Scrollbar(self.window)

# Botões
        self.btnViewAll = Button(self.window, text="Ver todos")
        self.btnBuscar = Button(self.window, text="Buscar")
        self.btnInserir = Button(self.window, text="Inserir")
        self.btnUpdate = Button(self.window, text="Atualizar Selecionados")
        self.btnDel = Button(self.window, text="Deletar Selecionados")
        self.btnClose = Button(self.window, text="Fechar")

#Associar os objetos criados ao Grid da Janela
        self.lblnome.grid(row=0, column=0)
        self.lblsobrenome.grid(row=1, column=0)
        self.lblemail.grid(row=2, column=0)
        self.lblcpf.grid(row=3, column=0)

        self.entNome.grid(row=0, column=1, padx=50, pady=50)
        self.entSobrenome.grid(row=1, column=1)
        self.entEmail.grid(row=2, column=1)
        self.entCPF.grid(row=3, column=1)

        self.listClientes.grid(row=0, column=2, rowspan=10)
        self.scrollClientes.grid(row=0, column=6, rowspan=10)

        self.btnViewAll.grid(row=4, column=0, columnspan=2)
        self.btnBuscar.grid(row=5, column=0, columnspan=2)
        self.btnInserir.grid(row=6, column=0, columnspan=2)
        self.btnUpdate.grid(row=7, column=0, columnspan=2)
        self.btnDel.grid(row=8, column=0, columnspan=2)
        self.btnClose.grid(row=9, column=0, columnspan=2)

#Conectando o Scrollbar com a ListBox
        self.listClientes.configure(yscrollcommand=self.scrollClientes.set)
        self.scrollClientes.configure(command=self.listClientes.yview)

#Adicionando estilo (swag)
        for child in self.window.winfo_children():
            widget_class = child.__class__.__name__
            if widget_class == "Button":
                child.grid_configure(sticky='WE', padx=self.x_pad, pady=self.y_pad)
            elif widget_class == "Listbox":
                child.grid_configure(padx=0, pady=0, sticky='NS')
            elif widget_class == "Scrollbar":
                child.grid_configure(padx=0, pady=0, sticky='NS')
            else:
                child.grid_configure(padx=self.x_pad, pady=self.y_pad, sticky='N')

    def run(self):
        self.window.mainloop()
