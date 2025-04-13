from domain.customers.controllers.customer_controller import CustomerController

from domain.employees.controllers.employee_controller import EmployeeController

from domain.order.controllers.order_controller import OrderController
from domain.order.controllers.order_details_controller import OrderDetailsController
from domain.order.controllers.shippers_controller import ShippersController

from domain.product.controllers.categories_controller import CategoriesController
from domain.product.controllers.product_controller import ProductController
from domain.product.controllers.suppliers_controller import SupliersController

from domain.report.controllers.report_controller import ReportController
from main_view import mv

#TODO?: Provavelmente todos os controllers vão ter que importar o northwind e passar pros DAO -> Ainda pensando sobre como fazer

class MainController():
    
    def __init__(self):
        self.order_controller = OrderController(self) #Adicionei self dentro
        self.report_controller = ReportController(self)

        self.root = tk.Tk()
        self.root.title('Vendas de Produtos')
        self.view = mv.MainView(self.root, self)

        self.root.mainloop()

    def registerOrder(self):
        self.order_controller.registerOrder()

    def consultOrder(self):
        self.order_controller.consultOrder()

    def consultReport(self):
        self.report_controller.consultReport()

    #def create_order(self): # TODO: Chamar na view
    #    return self.order_controller.create_order()