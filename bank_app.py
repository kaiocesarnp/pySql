#Conectando o Backend com o Frontend
#Nesse arquivo, importaremos os outros dois componentes que criamos e faremos a sua declaração por meio da variável app.

#from bank_gui import *
import bank_backend as core
from bank_gui import Gui
from tkinter import END

app = None

def view_command():
    rows = core.view()
    app.listClientes.delete(0, END)
    for r in rows:
        app.listClientes.insert(END, r)
    print("Adicionado!")

def search_command():
    app.listClientes.delete(0, END)

    rows = core.search(app.txtNome.get(), app.txtSobrenome.get(), app.txtEmail.get(), app.txtCPF.get())
    for r in rows:
        app.listClientes.insert(END, r)

def insert_command():
    core.insert(app.txtNome.get(), app.txtSobrenome.get(), app.txtEmail.get(), app.txtCPF.get())
    view_command()

def update_command():
    core.update(selected[0], app.txtNome.get(), app.txtSobrenome.get(), app.txtEmail.get(), app.txtCPF.get())
    view_command()

def del_command():
    id = selected[0]
    core.delete(id)
    view_command()

def getSelectedRow(event):
    global selected
    index = app.listClientes.curselection()[0]
    selected = app.listClientes.get(index)
    app.entNome.delete(0, END)
    app.entNome.insert(END, selected[1])
    app.entSobrenome.delete(0, END)
    app.entSobrenome.insert(END, selected[2])
    app.entEmail.delete(0, END)
    app.entEmail.insert(END, selected[3])
    app.entCPF.delete(0, END)
    app.entCPF.insert(END, selected[4])
    return selected

if __name__ == "__main__":
    app = Gui()
    app.listClientes.bind('<<ListboxSelect>>', getSelectedRow)

    app.btnViewAll.configure(command = view_command)
    app.btnBuscar.configure(command = search_command)
    app.btnInserir.configure(command = insert_command)
    app.btnUpdate.configure(command = update_command)
    app.btnDel.configure(command = del_command)
    app.btnClose.configure(command = app.window.destroy)
    app.run()


#A conexão da estrutura interna da aplicação (Backend) com sua “estrutura externa”(Fronted) é realizada, primeiramente coma declaração de uma variável que denominamos genericamente de app.
#Ao estudar o código verifique que ela recebe um valor do tipo None. Na linha import Backend as core realizamos a importação do script bank_backend.py.
#O comando App = Gui () faz que a variável app se torne uma instância da classe Gui.Através da variável app podemos acessar os elementos que estabelecemos para a janela. Por exemplo app.btBuscar(command=search_command) etc.
#A função def view_command() é a função de visualização dos resultados.
#As funções search_command() e insert_command() realizam a busca e a inserçãode dados no banco respectivamente.
#A função getSelectedRow(event) armazena os valores informados e alimenta os campos de input com as informações.

#A estrutura final do programa se organiza da seguinte forma:

#Realizar a importação da estrutura gráfica e do Backend.
#Declarar e carregar a variável app com app = None.
#Declarar as funções de comando view_command etc.
#Declarar a função getSelectRow.
#Instanciar a variával app em app = Gui().
#Vincular a caixa de menssagens app.listClientes.bind.
#Vincular funções de comando aos objetos (app.btnViewAll.configure).
#Iniciar às janelas em app.run().
#Na função getSelectRow(event), foi declarada uma variável global, ou seja, ela pode ser acessada de qualquer parte do código.

#Importante:
#A criação de variáveis globais sem o devido cuidado poderá comprometer a segurança da aplicação. Recomenda-se utilizar as melhores práticas de programação neste sentido.

#Note que em seguida, foram realizadas as seguintes instruções:
#Retorno do index do item escolhido (este índice será a primeira posição do vetor que a função curselection() retorna);
#Armazenamento do item escolhido na variável global selected;
#Limpeza e preenchimento dos campos do input (entry).
    
