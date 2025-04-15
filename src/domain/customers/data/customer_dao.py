from database.database_drive import database
from ..models.customer_model import Customer
from utils.errors.not_found_exception import NotFoundException

class CustomerDataAccess():
    def __init__(self):
        pass

    @staticmethod
    def get_customer_by_name(name: str):
        customer = None

        with database() as connection:
            with connection.cursor() as session:
                session.execute(f"select * from northwind.customers where companyname = '{name}';")
                row = session.fetchall()
                if(len(row) == 0):
                    raise NotFoundException("Cliente não encontrado.")
                customer = Customer(*row[0])
        return customer
    
    @staticmethod
    def get_customer_by_name_safe(name: str):
        customer = None

        with database() as connection:
            with connection.cursor() as session:
                session.execute(f"select * from northwind.customers where companyname = %s;", (name, ))
                row = session.fetchall()
                if(len(row) == 0):
                    raise NotFoundException("Cliente não encontrado.")
                customer = Customer(*row[0])
        return customer