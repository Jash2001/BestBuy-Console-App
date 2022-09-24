from bo import *
from domain import *
from utility import *
class SupplierDAO:

    def obtain_all_suppliers(self):
        '''Fill your code here'''
        dbObj = DBConnection()
        mydb = dbObj.get_connection()
        mycursor = mydb.cursor()
        query = query = "select * from supplier"
        mycursor.execute(query)
        result = mycursor.fetchall()
        item_list = list()
        for row in result:
            item = "%-20s %-20s %-20s %-20s %-20s"%(str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]))
            item_list.append(item)
        return item_list
        
    def obtain_supplier_by_id(self,id):
        '''Fill your code here'''
        dbObj = DBConnection()
        mydb = dbObj.get_connection()
        mycursor = mydb.cursor()
        query = "SELECT id FROM supplier WHERE id= " + str(id)
        mycursor.execute(query)
        result = mycursor.fetchall()
        if len(result) == 0:
            return None
        return result[0][0]
        
    def display_suppliers(self):
        '''Fill your code here'''
        return None
        
