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
                
                

    # @staticmethod
    # def employees_report(inital_date: date, final_date: date):
    #     report = []
    #     with database() as connection:
    #         with connection.cursor() as session:
    #             session.execute(f"""select e.firstname, e.lastname, sum(d.quantity) as total_quantity, sum(d.unitprice * d.quantity) as total_value
    #                                 from northwind.orders o join northwind.order_details d on o.orderid = d.orderid
    #                                 join northwind.employees e on o.employeeid = e.employeeid
    #                                 where o.orderdate between '{inital_date}' and '{final_date}'
    #                                 group by e.firstname, e.lastname
    #                                 order by total_value desc;""")
    #             rows = session.fetchall()

    #             if len(rows) == 0:
    #                 raise NotFoundException(f"Nenhum pedido encontrado no intervalo '{inital_date}' - '{final_date}'.")
                
    #             for row in rows:
    #                 report.append((f"{row[0]} {row[1]}", row[2], f"R${row[3]:,.2f}"))
    #     return report
    
    @staticmethod
    def employees_report(inital_date: date, final_date: date):
        report = []
        with database() as connection:
            with connection.cursor() as session:
                session.execute(f"""select e.firstname, e.lastname, sum(d.quantity) as total_quantity, sum(d.unitprice * d.quantity) as total_value
                                    from northwind.orders o join northwind.order_details d on o.orderid = d.orderid
                                    join northwind.employees e on o.employeeid = e.employeeid
                                    where o.orderdate between %s and %s
                                    group by e.firstname, e.lastname
                                    order by total_value desc;""", 
                                    (inital_date, final_date))
                rows = session.fetchall()

                if len(rows) == 0:
                    raise NotFoundException(f"Nenhum pedido encontrado no intervalo '{inital_date}' - '{final_date}'.")
                
                for row in rows:
                    report.append((f"{row[0]} {row[1]}", row[2], f"R${row[3]:,.2f}"))
        return report
                
                
