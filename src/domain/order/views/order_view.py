import tkinter as tk
from tkinter import messagebox


class registerOrderView(tk.Toplevel):

  def __init__(self, OrderController):
    self.OrderController = OrderController

    tk.Toplevel.__init__(self)
    self.geometry('400x400')
    self.title("Cadastrar Pedido")

    #CAMPOS DE ENTRADAS
    self.frameOrderEmployeeFName = tk.Frame(self)
    self.frameOrderEmployeeFName.pack()
    self.frameOrderEmployeeLName = tk.Frame(self)
    self.frameOrderEmployeeLName.pack()
    self.frameOrderCustomer = tk.Frame(self)
    self.frameOrderCustomer.pack()
    self.frameOrderDate = tk.Frame(self)
    self.frameOrderDate.pack()
    self.frameOrderProduct = tk.Frame(self)
    self.frameOrderProduct.pack()
    self.frameOrderQuantity = tk.Frame(self)
    self.frameOrderQuantity.pack()

    #RÓTULOS DAS ENTRADAS
    self.labelOrderEmployeeFName = tk.Label(self.frameOrderEmployeeFName, text="Nome do Vendedor: ")
    self.labelOrderEmployeeFName.pack(side='left')
    self.labelOrderEmployeeLName = tk.Label(self.frameOrderEmployeeLName, text="Sobrenome do Vendedor: ")
    self.labelOrderEmployeeLName.pack(side='left')
    self.labelOrderCustomer = tk.Label(self.frameOrderCustomer, text="Nome do Cliente: ")
    self.labelOrderCustomer.pack(side='left')
    self.labelOrderDate = tk.Label(self.frameOrderDate, text="Data (YYYY-MM-DD): ")
    self.labelOrderDate.pack(side='left')
    self.labelOrderProduct = tk.Label(self.frameOrderProduct, text="Nome do Produto: ")
    self.labelOrderProduct.pack(side='left')
    self.labelOrderQuantity = tk.Label(self.frameOrderQuantity, text="Quantidade: ")
    self.labelOrderQuantity.pack(side='left')

    #DADOS DE ENTRADAS
    self.employee_fname = tk.Entry(self.frameOrderEmployeeFName, width=20)
    self.employee_fname.pack(side='left')
    self.employee_lname = tk.Entry(self.frameOrderEmployeeLName, width=20)
    self.employee_lname.pack(side='left')
    self.customer_name = tk.Entry(self.frameOrderCustomer, width=20)
    self.customer_name.pack(side='left')
    self.order_date = tk.Entry(self.frameOrderDate, width=20)
    self.order_date.pack(side='left')
    self.product_name = tk.Entry(self.frameOrderProduct, width=20)
    self.product_name.pack(side='left')
    self.quantity = tk.Entry(self.frameOrderQuantity, width=20)
    self.quantity.pack(side='left')

    self.frameListbox = tk.Listbox(self, height=6, width=40)
    self.frameListbox.pack()

    self.state = tk.IntVar()
    self.frameCheckbox = tk.Checkbutton(self, text="Modo Injection", variable=self.state)
    self.frameCheckbox.pack()

    self.frameButton = tk.Frame(self)
    self.frameButton.pack()

    self.buttonSubmit = tk.Button(self.frameButton, text='Cadastrar Pedido')
    self.buttonSubmit.pack(side='left')
    self.buttonSubmit.bind('<Button>', OrderController.enterRegisterHandler)

    self.buttonAdd = tk.Button(self.frameButton, text='Adicionar Produto')
    self.buttonAdd.pack(side='left')
    self.buttonAdd.bind('<Button>', OrderController.enterAddHandler)

  def showView(self, title, msg):
    messagebox.showinfo(title, msg)


#--------------------------------------------------------------
class consultOrderView(tk.Toplevel):

  def __init__(self, OrderController):
    self.OrderController = OrderController

    tk.Toplevel.__init__(self)
    self.geometry('400x200')
    self.title("Consultar Pedido")

    self.frameOrder = tk.Frame(self)
    self.frameOrder.pack()
    self.frameButton = tk.Frame(self)
    self.frameButton.pack()

    self.labelOrderId = tk.Label(self.frameOrder, text="Id do Pedido: ")
    self.labelOrderId.pack(side='left')

    self.order_id = tk.Entry(self.frameOrder, width=20)
    self.order_id.pack(side='left')

    self.buttonSubmit = tk.Button(self.frameButton, text='Consultar')
    self.buttonSubmit.pack(side='left')
    self.buttonSubmit.bind('<Button>', OrderController.searchHandler)

  def showView(self, title, msg):
    messagebox.showinfo(title, msg)