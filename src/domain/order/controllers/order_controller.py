from ..data.order_dao import OrderDataAccess
from ..data.order_details_dao import OrderDetailsDataAccess
from domain.employees.data.employee_dao import EmployeeDataAccess
from domain.customers.data.customer_dao import CustomerDataAccess
from domain.product.data.product_dao import ProductDataAccess
from ..views.order_view import OrderView
from ..models.order_model import Order
from ..models.order_details_model import OrderDetails
from utils.error_handler import ErrorHandler
from datetime import date
from database.database_drive import database
from src.utils.errors.out_of_stock_exception import OutOfStockException

class OrderController():
    def __init__(self):
        pass

    def create_order(self): # Callback
        connetion = database()
        try: 
            #TODO: Pegar tudo das views
            fn, ln = "Nancy", "Davolio"
            cn = "Around the Horn"
            pn = ["Chai", "Chang"]
            qtds = [20, 5]
            discounts = [0.0, 2.1]

            employee = EmployeeDataAccess.get_employee_by_name(fn, ln)
            customer = CustomerDataAccess.get_customer_by_name(cn)
            
            products = []
            products_ids = []

            for name, qtd, discount in zip(pn, qtds, discounts):
                product = ProductDataAccess.get_product_by_name(name) # Produto por produto, porque se um não existir, é mais fácil de indicar qual

                # Verificação de estoque
                if(product.units_in_stock < qtd):
                    raise OutOfStockException("Não há unidades suficientes para o pedido")
                
                products.append((product, qtd, discount))
                products_ids.append(product.product_id)

            order_id = OrderDataAccess.get_last_order_id() + 1 # Gera um id para o produto baseado nos que já existem
            order = Order(order_id, customer.customer_id, employee.employee_id, date.today(), date.today(), date.today(), 10.36, "name", "address", "city", "region", "postal", "country", None)
            
            details_list = []
            
            for product in products: # Um details para cada produto
                order_details = OrderDetails(order_id, product[0].product_id, product[0].unit_price, product[1], product[2])
                details_list.append(order_details)
                
            
            # Executando tudo em uma mesma transação
            session = connetion.cursor()

            OrderDataAccess.create_order(order, session)
            OrderDetailsDataAccess.create_many_order_details(details_list, session)
            ProductDataAccess.update_many_products_stock(products_ids, qtds, session)

            session.close()
            connetion.commit()
            # Fim da transação;

        except Exception as error:
            connetion.rollback()
            ErrorHandler.showError(ErrorHandler.catchError(error))