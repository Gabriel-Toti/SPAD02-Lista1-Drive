from ..data.order_dao import OrderDataAccess
from ..data.order_details_dao import OrderDetailsDataAccess
from domain.employees.data.employee_dao import EmployeeDataAccess
from domain.customers.data.customer_dao import CustomerDataAccess
from domain.product.data.product_dao import ProductDataAccess
from ..views import order_view
from ..models.order_model import Order
from ..models.order_details_model import OrderDetails
from utils.error_handler import ErrorHandler
from datetime import date, datetime
from database.database_drive import database
from src.utils.errors.out_of_stock_exception import OutOfStockException
from tkinter import END


class OrderController():
    def __init__(self, controller):
        self.controller = controller
        self.list = []

    def registerOrder(self):
        self.orderRegisterView = order_view.registerOrderView(self)

    def consultOrder(self):
        self.orderConsultView = order_view.consultOrderView(self)

#------------------------------------

    def enterRegisterHandler(self, event):
        try:
            self.checkState(event)
            
            first_name = self.orderRegisterView.employee_fname.get()
            last_name = self.orderRegisterView.employee_lname.get()
            customer_name = self.orderRegisterView.customer_name.get()
            order_date = self.orderRegisterView.order_date.get()

            if(first_name == '' or last_name == '' or customer_name == '' or order_date == ''):
                raise ValueError('Há campos em branco!')

            try:
                datetime.strptime(order_date, '%Y-%m-%d')
            except ValueError:
                raise ValueError('Data inválida! Use o formato AAAA-MM-DD.')

            if not self.list:
                raise ValueError('Adicione pelo menos um produto!')
            
            
            self.__create_order(first_name, last_name, customer_name, self.list, order_date)


            self.orderRegisterView.showView('Sucesso', 'Pedido cadastrado!')
            self.orderRegisterView.state.set(0)
            self.list.clear()
            self.clearRegisterHandler(event)
        except Exception as error:
            ErrorHandler.showError(ErrorHandler.catchError(error))

#------------------------------------

    def enterAddHandler(self, event):

        product_name = self.orderRegisterView.product_name.get().strip()
        quantity = self.orderRegisterView.quantity.get().strip()

        if(product_name == ''):
            raise ValueError("Preencha o nome do produto.")
            
        if (quantity == ''):
            raise ValueError('Preencha a quantidade!')
        
        if not quantity.isdigit() or int(quantity) <= 0:
            raise ValueError("'Quantidade inválida!'")

        self.list.append((product_name, int(quantity)))
        self.orderRegisterView.frameListbox.insert(END, f"Produto: {product_name} | Quantidade: {quantity}")
        
        self.orderRegisterView.product_name.delete(
            0, len(self.orderRegisterView.product_name.get()))
        self.orderRegisterView.quantity.delete(
            0, len(self.orderRegisterView.quantity.get()))

#------------------------------------

    def searchHandler(self, event):

            order_id = self.orderConsultView.order_id.delete(
                0, len(self.orderConsultView.order_id.get()))

            report_data = self.__get_order_report(order_id)
            
            if (report_data is not None):
                report = ''
                #str += f'Pedido: {order.order_id}\n'
                #str += f'Vendedor: {employee.first_name} {employee.last_name}\n'
                #str += f'Cliente: {customer.customer_name}\n'
                #str += f'Data: {order.order_date}\n'
                #str += f'Itens do Pedido: \n'
                #for i in self.order_details:
                #  str += f'{i.product_name} - {i.quantity} = {i.total}\n'

                self.orderConsultView.showView('Dados do Pedido', report)
                self.orderConsultView.order_id.delete(
                    0, len(self.orderConsultView.order_id.get()))
                return
            self.orderConsultView.showView('Erro', 'Pedido não encontrado!')

#------------------------------------

    def clearRegisterHandler(self, event):
        self.orderRegisterView.employee_fname.delete(
            0, len(self.orderRegisterView.employee_fname.get()))
        self.orderRegisterView.employee_lname.delete(
            0, len(self.orderRegisterView.employee_lname.get()))
        self.orderRegisterView.customer_name.delete(
            0, len(self.orderRegisterView.customer_name.get()))
        self.orderRegisterView.order_date.delete(
            0, len(self.orderRegisterView.order_date.get()))
        self.orderRegisterView.product_name.delete(
            0, len(self.orderRegisterView.product_name.get()))
        self.orderRegisterView.quantity.delete(
            0, len(self.orderRegisterView.quantity.get()))
        self.orderRegisterView.state.set(0)
        self.orderRegisterView.frameListbox.delete(0, END)
        

    def clearConsultHandler(self, event):
        self.orderConsultView.order_id.delete(
            0, len(self.orderConsultView.order_id.get()))

#------------------------------------

    def checkState(self, event):
        state = self.orderRegisterView.state.get()
        if state == 1:
            #CADASTRO DO TIPO INJECTION
            # enterInjectionAddHandler()
            print("injection")
        else:
            print("sem injection")
            return

#------------------------------------

    def __create_order(self, first_name: str, last_name: str, customer_name: str, products_data: list[tuple[str, int]], order_date: date): # Callback
            connetion = database()
            try: 
                employee = EmployeeDataAccess.get_employee_by_name(first_name, last_name)
                customer = CustomerDataAccess.get_customer_by_name(customer_name)
                
                products = []
                products_ids = []
                quantities = []

                for name, quantity in products_data:
                    product = ProductDataAccess.get_product_by_name(name) # Produto por produto, porque se um não existir, é mais fácil de indicar qual

                    # Verificação de estoque
                    if(product.units_in_stock < quantity):
                        raise OutOfStockException(f"Não há unidades suficientes de '{product.product_name}' para o pedido.")
                    
                    products.append((product, quantity))
                    quantities.append(quantity)
                    products_ids.append(product.product_id)

                order_id = OrderDataAccess.get_last_order_id() + 1 # Gera um id para o produto baseado nos que já existem
                order = Order(order_id, customer.customer_id, employee.employee_id, order_date)
                
                details_list = []
                
                for product in products: # Um details para cada produto
                    order_details = OrderDetails(order_id, product[0].product_id, product[0].unit_price, product[1])
                    details_list.append(order_details)
                    
                
                # Executando tudo em uma mesma transação
                session = connetion.cursor()

                OrderDataAccess.create_order(order, session)
                OrderDetailsDataAccess.create_many_order_details(details_list, session)
                ProductDataAccess.update_many_products_stock(products_ids, quantities, session)

                session.close()
                connetion.commit()
                # Fim da transação;

            except Exception as error:
                connetion.rollback()
                raise error
    def __get_order_report(self, order):
        #LÓGICA QUE VERIFICA SE PEDIDO EXISTE NO BD E DEVOLVE RESULTADO (LIST)
        pass
