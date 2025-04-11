from ..data.order_dao import OrderDataAccess
from ..views.order_view import OrderView
from ..models.order_model import Order
from ..models.order_details_model import OrderDetails
from psycopg import OperationalError
from utils.error_handler import ErrorHandler
from datetime import date

class OrderController():
    def __init__(self):
        pass

    def get_all_orders(self):
        try:
            return OrderDataAccess.get_all_orders()
        except OperationalError as error:
            ErrorHandler.showError(ErrorHandler.catchError(error))
        except TypeError as error:
            ErrorHandler.showError(ErrorHandler.catchError(error))
        except Exception as error:
            ErrorHandler.showError(ErrorHandler.catchError(error))
    
    def create_order(self): #? Aqui eu vou chamar a view ou isso vai ser um handler?
        try:
            order = Order(1, "1", 1, date.today(), date.today(), date.today(), 1.3, "name", "address", "city", "region", "postal", "country", 0)
            order_details = OrderDetails(1, 2, 10, 1, 0)
            return OrderDataAccess.create_order(order, order_details)
        except OperationalError as error:
            ErrorHandler.showError(ErrorHandler.catchError(error))
        except TypeError as error:
            ErrorHandler.showError(ErrorHandler.catchError(error))
        except Exception as error:
            ErrorHandler.showError(ErrorHandler.catchError(error))