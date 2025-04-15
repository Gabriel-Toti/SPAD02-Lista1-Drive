from database.database_drive import database
from ..models.employee_model import Employee
from utils.errors.not_found_exception import NotFoundException
class EmployeeDataAccess():
    def __init__(self):
        pass

    @staticmethod
    def get_employee_by_name(first_name: str, last_name: str):
        employee = None
        with database() as connection:
            with connection.cursor() as session:
                print(f"select * from northwind.employees where firstname = '{first_name}' and lastname = '{last_name}';")
                #print("Nancy'; delete from northwind.order_details where orderid=11078; --")
                session.execute(f"select * from northwind.employees where firstname = '{first_name}' and lastname = '{last_name}';")
                row = session.fetchall()
                if(len(row) == 0):
                    raise NotFoundException("Empregado não encontrado.")
                employee = Employee(*row[0])
        return employee

    @staticmethod
    def get_employee_by_name_safe(first_name: str, last_name: str):
        employee = None
        with database() as connection:
            with connection.cursor() as session:
                print(f"select * from northwind.employees where firstname = '{first_name}' and lastname = '{last_name}';")
                #"Nancy'; delete from northwind.order_details where orderid=11078; --"
                session.execute(f"select * from northwind.employees where firstname = %s and lastname = %s;", (first_name, last_name))
                row = session.fetchall()
                if(len(row) == 0):
                    raise NotFoundException("Empregado não encontrado.")
                employee = Employee(*row[0])
        return employee
