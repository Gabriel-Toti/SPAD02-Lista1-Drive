from psycopg import Connection
from ..models.order_model import Order
from ..models.order_details_model import OrderDetails
from database.database_drive import database

class OrderDataAccess():
    def __init__(self):
        pass

    @staticmethod
    def get_all_orders():
        try:
            with database() as connection:
                with connection.cursor() as session:
                    session.execute("select * from northwind.orders order by orderid asc")

                    orders = []
                    rows = session.fetchall()
                    for row in rows:
                        orders.append(Order(*row))
        except TypeError as error:
            raise error
        except Exception as error:
            raise error
                    
        return orders
    
    @staticmethod
    def create_order(order: Order, order_details: OrderDetails): 
    #OrderDetails criado pelo controller do Order e utilizado pelo controller principal para juntar tudo

        # Cria as tuplas para os dados    
        order_data = order.attributes()

        print(order_data)

        #Executa a consulta
        with database() as connection:
            with connection.cursor() as session:
                session.execute(f"""insert into northwind.orders values {order_data};""")
                # session.execute("select * from northwind.orders order by orderid asc")
