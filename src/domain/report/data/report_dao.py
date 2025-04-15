from datetime import date
from database.database_drive import database
from utils.errors.not_found_exception import NotFoundException
class ReportDataAccess():
    def __init__(self):
        pass

    @staticmethod
    def order_report(order_id: int):
        report = {
            "order_id": None,
            "order_date": None,
            "company_name": None,
            "employee_name": None,
            "products": []
        }
        with database() as connection:
            with connection.cursor() as session:
                session.execute(f"""select o.orderid, o.orderdate, c.companyname, e.firstname,
                                    e.lastname, p.productname, d.unitprice, d.quantity
                                    from northwind.orders o join northwind.customers c on o.customerid = c.customerid
                                    join northwind.employees e on o.employeeid = e.employeeid
                                    join northwind.order_details d on o.orderid = d.orderid
                                    join northwind.products p on d.productid = p.productid
                                    where o.orderid = {order_id};
                                """)
                rows = session.fetchall()

                if len(rows) == 0:
                    raise NotFoundException(f"Pedido com id {order_id} não encontrado.")

                report["order_id"] = rows[0][0]
                report["order_date"] = rows[0][1].strftime("%d/%m/%Y")
                report["company_name"] = rows[0][2]
                report["employee_name"] = f"{rows[0][3]} {rows[0][4]}"
                
                products_data = []

                for row in rows:
                    products_data.append((row[5], row[7], f"{(row[6] * row[7]):.2f}"))
                
                report["products"] = products_data
        return report
                
                

    @staticmethod
    def employees_report(inital_date: date, end_date: date):
        pass