from bo import *
from domain import *
from utility import *
class ProductDAO:
    def obtain_all_products(self):
        '''Fill your code here'''
        dbObj = DBConnection()
        mydb = dbObj.get_connection()
        mycursor = mydb.cursor()
        query = "SELECT * FROM product"
        mycursor.execute(query)
        result = mycursor.fetchall()
        return result

    def add_product(self,product):
        '''Fill your code here'''
        name = product.get_name()
        color = product.get_color()
        material = product.get_material()
        price = product.get_price()
        quantity = product.get_quantity()
        brand = product.get_brand()
        productType = product.get_product_type()
        productCategory = product.get_product_category()
        active = product.get_active()
        dbObj = DBConnection()
        mydb = dbObj.get_connection()
        mycursor = mydb.cursor()
        s = "SELECT name,brand_id,color,material,price,active,quantity,product_type_id,product_category_id FROM product where name = '" + name + "' and brand_id = " + str(brand) + " and color = '" + color + "' and material = '" + material + "' and price = " + str(price) + " and active = " + str(active) + " and quantity = " + str(quantity) + " and product_type_id = " + str(productType) + " and product_category_id = " + str(productCategory)
        print(s)
        mycursor.execute(s)
        result = mycursor.fetchall()
        print(result)
        if len(result) != 0:
            return False 
        else:
            mycursor.execute("select * from product")
            result = mycursor.fetchall()
            rc = len(result) + 1
            sql = "INSERT INTO product (id,name,brand_id,color,material,price,active,quantity,product_type_id,product_category_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (rc, name, brand, color, material, price, active, quantity, productType, productCategory)
            mycursor.execute(sql, val)
            mydb.commit()
            return True

    def display_all_products(self):
        '''Fill your code here'''
        print("Product Details:")
        print("%-20s %-20s %-20s %-20s %-20s %-20s %-20s %-20s %-20s\n"%("Id", "Product Name","Brand","Color","Material","Price","Available Quantity","Product Type","Product Category"))
        dbObj = DBConnection()
        mydb = dbObj.get_connection()
        mycursor = mydb.cursor()
        query = "select p.id, p.name, b.name, p.color, p.material, p.price, p.quantity, pt.name, pc.name from product p, brand b, product_type pt, product_category pc where p.brand_id = b.id and p.product_type_id = pt.id and p.product_category_id = pc.id"
        mycursor.execute(query)
        result = mycursor.fetchall()
        for i in result:
            print("%-20s %-20s %-20s %-20s %-20s %-20s %-20s %-20s %-20s\n"%(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]))

    def obtain_product_by_name(self,name):
        '''Fill your code here'''
        dbObj = DBConnection()
        mydb = dbObj.get_connection()
        mycursor = mydb.cursor()
        query = "SELECT id FROM product WHERE name= '" + name + "'"
        mycursor.execute(query)
        result = mycursor.fetchall()
        if len(result) == 0:
            return None
        return result[0][0]

    def obtain_product_by_id(self,id):
        dbObj = DBConnection()
        mydb = dbObj.get_connection()
        mycursor = mydb.cursor()
        query = "SELECT id FROM product WHERE id= " + str(id)
        mycursor.execute(query)
        result = mycursor.fetchall()
        if len(result) == 0:
            return None
        return Product(result[0][0])

    def update_product(self, product):
        '''Fill your code here'''
        name = product.get_name()
        color = product.get_color()
        material = product.get_material()
        price = product.get_price()
        quantity = product.get_quantity()
        active = product.get_active()
        id = product.get_id()
        dbObj = DBConnection()
        mydb = dbObj.get_connection()
        mycursor = mydb.cursor()
        query = "UPDATE product SET name = '" + name + "', color = '" + color + "', material = '" + material + "', price = " + str(price) + ", quantity = " + str(quantity) + ", active = " + str(active) + " WHERE id = " + str(id) + ""
        mycursor.execute(query)
        mydb.commit()
        return True

    def display_product(self,product):
        '''Fill your code here'''
        print("Product Details:")
        print("%-20s %-20s %-20s %-20s %-20s %-20s %-20s %-20s %-20s\n"%("Id", "Product Name","Brand","Color","Material","Price","Available Quantity","Product Type","Product Category"))
        dbObj = DBConnection()
        mydb = dbObj.get_connection()
        mycursor = mydb.cursor()
        query = "select p.id, p.name, b.name, p.color, p.material, p.price, p.quantity, pt.name, pc.name from product p, brand b, product_type pt, product_category pc where p.id = " + str(product) + " and p.brand_id = b.id and p.product_type_id = pt.id and p.product_category_id = pc.id"
        mycursor.execute(query)
        result = mycursor.fetchall()
        for i in result:
            print("%-20s %-20s %-20s %-20s %-20s %-20s %-20s %-20s %-20s\n"%(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]))











            
    
