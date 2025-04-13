from database.database_drive import database
from ..models.product_model import Product
from psycopg import Cursor
from utils.logger import logger
from utils.errors.not_found_exception import NotFoundException

class ProductDataAccess():
    def __init__(self):
        pass

    @staticmethod
    def get_product_by_name(name: str):
        product = None
        with database() as connection:
            with connection.cursor() as session:
                session.execute(f"select * from northwind.products where productname = '{name}';")
                row = session.fetchall()
                if(len(row) == 0):
                    raise NotFoundException(f"Produto '{name}' não encontrado.")
                product = Product(*row[0])
        return product
    
    @staticmethod
    def update_many_products_stock(product_id: list[int], amount: list[int], session: Cursor): # Poderia ser feito com um trigger tbm, talvez fosse melhor
        values = []
        for data in zip(product_id, amount):
            values.append(data)
        
        session.execute(f"""update northwind.products
                         set unitsinstock = unitsinstock - o.amount, unitsonorder = unitsonorder + o.amount
                         from ( values 
                               {str(values).replace("[", "").replace("]", "")} 
                        ) as o(product_id, amount)
                         where productid = o.product_id;""")
        logger.log("Estoque atualizado com sucesso")
                