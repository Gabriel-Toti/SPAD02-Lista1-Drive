from psycopg import Connection
from ..models.order_model import Order
from database.database_drive import database
from utils.logger import logger
from psycopg import Cursor

class OrderDataAccess():
    def __init__(self):
        pass

    @staticmethod
    def get_last_order_id():
        id = None
        with database() as connection:
            with connection.cursor() as session:
                session.execute("select max(orderid) from northwind.orders;")
                row = session.fetchall()[0]
                id = row[0]
                    
        return id
    
    @staticmethod
    def create_order(order: Order, session: Cursor): # depende de outro DAO, então preciso do cursor pra manter dentro de uma mesma transação
    #OrderDetails criado pelo controller do Order e utilizado pelo controller principal para juntar tudo

        # Cria as tuplas para os dados    
        order_data = order.attributes()

        #Executa a consulta
        session.execute(f"""insert into northwind.orders values {order_data};""".replace("'None'", "null"))
        logger.log("Order inserida com sucesso.")
    
    @staticmethod
    def create_order_safe(order: Order, session: Cursor): # depende de outro DAO, então preciso do cursor pra manter dentro de uma mesma transação
    #OrderDetails criado pelo controller do Order e utilizado pelo controller principal para juntar tudo

        # Cria as tuplas para os dados    
        order_data = order.attributes(True)

        print(order_data)

        #Executa a consulta
        session.execute(f"""insert into northwind.orders values (%s, %s, %s, %s);""", order_data)
        logger.log("Order inserida com sucesso.")
