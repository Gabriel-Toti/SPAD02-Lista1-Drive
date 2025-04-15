from tkinter import Menu

class MainView():
    
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller

        self.root.geometry('400x200')

        self.menubar = Menu(self.root)
        self.orderMenu = Menu(self.menubar)
        self.reportMenu = Menu(self.menubar)

        #SUBMENU ORDER
        self.orderMenu.add_command(label='Cadastrar', command=self.controller.registerOrder)
        self.orderMenu.add_command(label='Consultar', command=self.controller.consultOrder)
        self.menubar.add_cascade(label="Pedidos", menu=self.orderMenu)
        
        #SUBMENU RANKING
        self.reportMenu.add_command(label='Ranking', command=self.controller.consultReport)
        self.menubar.add_cascade(label="Relatório", menu=self.reportMenu)

        self.root.config(menu=self.menubar)
