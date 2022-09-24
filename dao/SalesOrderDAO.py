from bo import *
from domain import *
from utility import *
from dao import UserDAO,SalesOrderItemDAO

class SalesOrderDAO:

    def obtain_all_sales_order(self):
        '''Fill your code here'''
        dbObj = DBConnection()
        mydb = dbObj.get_connection()
        mycursor = mydb.cursor()
        query = "SELECT * FROM sales_order"
        mycursor.execute(query)
        result = mycursor.fetchall()
        return result
         

    def add_sales_order(self,salesOrder):
        '''Fill your code here'''
        customer = salesOrder.get_customer()
        quantity = salesOrder.get_quantity()
        total_price = salesOrder.get_total_price()
        tax_amount = salesOrder.get_tax_amount()
        sales_lead = salesOrder.get_sales_lead()
        sales_date = salesOrder.get_sale_date()
        sales_date = str(sales_date).split(" ")
        sales_date = sales_date[0]
        query = "insert into sales_order (customer_id, quantity, total_price, tax_amount, sales_lead_id, sale_date) values (%s, %s, %s, %s, %s, %s)"
        args = (str(customer), str(quantity), str(total_price), str(tax_amount), str(sales_lead), sales_date)
        dbObj = DBConnection()
        mydb = dbObj.get_connection()
        mycursor = mydb.cursor()
        mycursor.execute(query, args)
        mydb.commit()
        return True

        
    def display_sales_order(self):
        '''Fill your code here'''
        print("Sales Order Details:")
        print("%-20s %-20s %-20s %-20s %-20s %-20s\n"%("User Name", "Order Quantity","Total Price","Tax Amount","Sales Lead","Sale Date"))
        dbObj = DBConnection()
        mydb = dbObj.get_connection()
        mycursor = mydb.cursor()
        query = "select u.name, s.quantity, s.total_price, s.tax_amount, u2.name, s.sale_date from user u, user u2, sales_order s where s.customer_id = u.id and s.sales_lead_id = u2.id"
        mycursor.execute(query)
        result = mycursor.fetchall()
        for i in result:
            print("%-20s %-20s %-20s %-20s %-20s %-20s\n"%(i[0], i[1], i[2], i[3], i[4], i[5]))