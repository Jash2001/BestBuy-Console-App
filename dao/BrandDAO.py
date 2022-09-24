from pydoc import stripid
from unittest import result
from domain import *
from utility import *

class BrandDAO:
    
    def obtain_all_brand(self):
        '''Fill your code here'''
        dbObj = DBConnection()
        mydb = dbObj.get_connection()
        mycursor = mydb.cursor()
        query = "SELECT * FROM brand"
        mycursor.execute(query)
        result = mycursor.fetchall()
        return result

    def add_brand(self,brand):
        '''Fill your code here'''
        name = brand.get_name()
        dbObj = DBConnection()
        mydb = dbObj.get_connection()
        mycursor = mydb.cursor()
        s = "SELECT name FROM brand where name = '" + name + "'"
        mycursor.execute(s)
        result = mycursor.fetchall()
        if len(result) != 0:
            return False 
        else:
            mycursor.execute("select * from brand")
            result = mycursor.fetchall()
            rc = len(result) + 1
            sql = "INSERT INTO brand (id,name) VALUES (%s, %s)"
            val = (rc, name)
            mycursor.execute(sql, val)
            mydb.commit()
            return True
    
    def display_brand(self):
        '''Fill your code here'''
        print("%-5s %-15s\n"%("Id","Name"))
        dbObj = DBConnection()
        mydb = dbObj.get_connection()
        mycursor = mydb.cursor()
        query = "SELECT * FROM brand"
        mycursor.execute(query)
        result = mycursor.fetchall()
        for i in result:
            print("%-5s %-15s\n"%(i[0],i[1]))
        

    def obtain_brand_by_id(self,id):
        '''Fill your code here'''
        dbObj = DBConnection()
        mydb = dbObj.get_connection()
        mycursor = mydb.cursor()
        query = "SELECT id FROM brand WHERE id= " + str(id)
        mycursor.execute(query)
        return mycursor.fetchall()[0][0]

