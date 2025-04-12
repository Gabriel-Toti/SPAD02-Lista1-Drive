from ..models.order_details_model import OrderDetails
from database.database_drive import database
from psycopg import Cursor
from utils.logger import logger
class OrderDetailsDataAccess():
    
    def __init__(self):
        pass

    @staticmethod
    def create_order_detail(order_details: OrderDetails, session: Cursor):
        order_data = order_details.attributes()
        session.execute(f"insert into northwind.order_details values {order_data};")
        logger.log("Detalhes adicionados com sucesso.")
    
    @staticmethod
    def create_many_order_details(order_details: list[OrderDetails], session: Cursor):
        details = []
        for detail in order_details:
            details.append(detail.attributes())

        order_data = str(details).replace("[", "").replace("]", "")

        session.execute(f"insert into northwind.order_details values {order_data};")
        logger.log("Detalhes adicionados com sucesso.")

