from bo import *
from domain import *
from utility import *
class ProductTypeDAO:
    
    def obtain_all_product_type(self):
        '''Fill your code here'''
        dbObj = DBConnection()
        mydb = dbObj.get_connection()
        mycursor = mydb.cursor()
        query = "SELECT * FROM product_type"
        mycursor.execute(query)
        result = mycursor.fetchall()
        return result

    def add_product_type(self,product_type):
        '''Fill your code here'''
        name = product_type.get_name()
        description = product_type.get_description()
        dbObj = DBConnection()
        mydb = dbObj.get_connection()
        mycursor = mydb.cursor()
        s = "SELECT name FROM product_type where name = '" + name + "'"
        mycursor.execute(s)
        result = mycursor.fetchall()
        if len(result) != 0:
            return False 
        else:
            mycursor.execute("select * from product_type")
            result = mycursor.fetchall()
            rc = len(result) + 1
            sql = "INSERT INTO product_type (id,name,description) VALUES (%s, %s, %s)"
            val = (rc, name, description)
            mycursor.execute(sql, val)
            mydb.commit()
            return True
        
    def display_product_type(self):
        '''Fill your code here'''
        print("%-5s %-15s %-15s\n"%("Id","Name","Description"))
        dbObj = DBConnection()
        mydb = dbObj.get_connection()
        mycursor = mydb.cursor()
        query = "SELECT * FROM product_type"
        mycursor.execute(query)
        result = mycursor.fetchall()
        for i in result:
            print("%-5s %-30s %-15s\n"%(i[0],i[1],i[2]))


    def obtain_product_type_by_id(self,id):
        '''Fill your code here'''
        dbObj = DBConnection()
        mydb = dbObj.get_connection()
        mycursor = mydb.cursor()
        query = "SELECT id FROM product_type WHERE id= " + str(id)
        mycursor.execute(query)
        return mycursor.fetchall()[0][0]
