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
                session.execute(f"select * from northwind.employees where firstname = '{first_name}' and lastname = '{last_name}';")
                row = session.fetchall()
                if(len(row) == 0):
                    raise NotFoundException("Empregado não encontrado.")
                employee = Employee(*row[0])
        return employee

