from domain.order.controllers.order_controller import OrderController

from domain.report.controllers.report_controller import ReportController
from main_view import mv
from tkinter import Tk

class MainController():
    
    def __init__(self):
        self.order_controller = OrderController(self) #Adicionei self dentro
        self.report_controller = ReportController(self)

        self.root = Tk()
        self.root.title('Vendas de Produtos')
        self.view = mv.MainView(self.root, self)

        self.root.mainloop()

    def registerOrder(self):
        self.order_controller.registerOrder()

    def consultOrder(self):
        self.order_controller.consultOrder()

    def consultReport(self):
        self.report_controller.consultReport()

