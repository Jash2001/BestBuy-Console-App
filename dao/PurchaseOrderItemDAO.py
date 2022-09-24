from bo import *
from domain import *
from utility import *
from dao import ProductDAO
class PurchaseOrderItemDAO:

    def obtain_all_purchase_order_items(self):
        '''Fill your code here'''
        dbObj = DBConnection()
        mydb = dbObj.get_connection()
        mycursor = mydb.cursor()
        query = "select poi.id, p.name, poi.quantity, poi.unit_price from purchase_order_item poi, product p where p.id = poi.product_id"
        mycursor.execute(query)
        result = mycursor.fetchall()
        item_list = list()
        for row in result:
            item = "%-20d %-20s %-20d %-20.2f"%(row[0], str(row[1]), row[2], row[3])
            item_list.append(item)
        return item_list
        

    def obtain_purchase_order_item_by_id(self,id):
        '''Fill your code here'''
        dbObj = DBConnection()
        mydb = dbObj.get_connection()
        mycursor = mydb.cursor()
        query = "SELECT * FROM purchase_order_item WHERE id= " + str(id)
        mycursor.execute(query)
        result = mycursor.fetchall()
        if len(result) == 0:
            return None
        return PurchaseOrderItem(result[0][0],result[0][1],result[0][2],result[0][3],result[0][4])