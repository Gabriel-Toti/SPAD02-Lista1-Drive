from database.database_drive import northwind
from main_controller import MainController
from main_view import MainView

print("Hello, World!")

session = northwind.cursor()
session.execute("select * from northwind.employees")

for row in session:
    print(row)

session.close()
northwind.close()