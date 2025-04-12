from domain.customers.controllers.customer_controller import CustomerController

from domain.employees.controllers.employee_controller import EmployeeController

from domain.order.controllers.order_controller import OrderController
from domain.order.controllers.order_details_controller import OrderDetailsController
from domain.order.controllers.shippers_controller import ShippersController

from domain.product.controllers.categories_controller import CategoriesController
from domain.product.controllers.product_controller import ProductController
from domain.product.controllers.suppliers_controller import SupliersController

from domain.report.controllers.report_controller import ReportController


#TODO?: Provavelmente todos os controllers vão ter que importar o northwind e passar pros DAO -> Ainda pensando sobre como fazer

class MainController():
    
    def __init__(self):
        self.order_controller = OrderController()
    
    def create_order(self): # TODO: Chamar na view
        return self.order_controller.create_order()