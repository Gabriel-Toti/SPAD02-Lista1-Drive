from database.database_drive import database
from ..models.employee_model import Employee
class EmployeeDataAccess():
    def __init__(self):
        pass

    @staticmethod
    def get_employee_by_name(first_name: str, last_name: str):
        employee = None
        with database() as connection:
            with connection.cursor() as session:
                session.execute(f"select * from northwind.employees where firstname = '{first_name}' and lastname = '{last_name}';")
                row = session.fetchall()[0]
                employee = Employee(*row)
        return employee

