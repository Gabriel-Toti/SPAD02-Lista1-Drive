from database.database_drive import database
from ..models.customer_model import Customer
class CustomerDataAccess():
    def __init__(self):
        pass

    @staticmethod
    def get_customer_by_name(name: str):
        customer = None

        with database() as connection:
            with connection.cursor() as session:
                session.execute(f"select * from northwind.customers where companyname = '{name}';")
                row = session.fetchall()[0]
                customer = Customer(*row)
        return customer