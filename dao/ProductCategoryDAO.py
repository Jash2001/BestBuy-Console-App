from bo import *
from domain import *
from utility import *
class ProductCategoryDAO:
    
    def obtain_all_product_category(self):
        '''Fill your code here'''
        dbObj = DBConnection()
        mydb = dbObj.get_connection()
        mycursor = mydb.cursor()
        query = "SELECT * FROM product_category"
        mycursor.execute(query)
        result = mycursor.fetchall()
        return result

    def add_product_category(self,product_category):
        '''Fill your code here'''
        name = product_category.get_name()
        description = product_category.get_description()
        dbObj = DBConnection()
        mydb = dbObj.get_connection()
        mycursor = mydb.cursor()
        s = "SELECT name FROM product_category where name = '" + name + "'"
        mycursor.execute(s)
        result = mycursor.fetchall()
        if len(result) != 0:
            return False 
        else:
            mycursor.execute("select * from product_category")
            result = mycursor.fetchall()
            rc = len(result) + 1
            sql = "INSERT INTO product_category (id,name,description) VALUES (%s, %s, %s)"
            val = (rc, name, description)
            mycursor.execute(sql, val)
            mydb.commit()
            return True
        
    def display_product_category(self):
        '''Fill your code here'''
        print("%-5s %-30s %-15s\n"%("Id","Name","Description"))
        dbObj = DBConnection()
        mydb = dbObj.get_connection()
        mycursor = mydb.cursor()
        query = "SELECT * FROM product_category"
        mycursor.execute(query)
        result = mycursor.fetchall()
        for i in result:
            print("%-5s %-30s %-15s\n"%(i[0],i[1],i[2]))

    def obtain_product_category_by_id(self,id):
        '''Fill your code here'''
        dbObj = DBConnection()
        mydb = dbObj.get_connection()
        mycursor = mydb.cursor()
        query = "SELECT id FROM product_category WHERE id= " + str(id)
        mycursor.execute(query)
        return mycursor.fetchall()[0][0]
