from domain.order.controllers.order_controller import OrderController
from domain.report.controllers.report_controller import ReportController

class MainController():
    
    def __init__(self):
        self.order_controller = OrderController()
    
    def create_order(self): # TODO: Chamar na view
        return self.order_controller.create_order()