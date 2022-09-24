from domain import *
from utility import *
from dao import RoleDAO

class UserDAO:
    def validate_login(self,username,password):
        user =None
        dbObj = DBConnection()
        mydb = dbObj.get_connection()
        mycursor = mydb.cursor()
        s="select * from user where username = '"+username+"' and password = '"+password+"'"
        mycursor.execute(s)
        roleDAO = RoleDAO()
        for x in mycursor:
            role = roleDAO.obtain_role_by_id(x[7])
            user=User(x[0],x[1],x[2],x[3],x[4],x[5],x[6],role)
        return user

    def obtain_users_by_role(self,name):
        '''Fill your code here'''
        dbObj = DBConnection()
        mydb = dbObj.get_connection()
        mycursor = mydb.cursor()
        query = "select u.id,u.name,u.username,u.password,u.mobile_number,u.email,u.address from user u, role r where u.role_id = r.id and r.name = '" + name + "'"
        mycursor.execute(query)
        result = mycursor.fetchall()
        item_list = list()
        for row in result:
            item = "%-20d %-20s %-20s %-20s %-20s %-20s"%(row[0], row[1], row[2], row[3], row[4], row[5])
            item_list.append(item)
        return item_list

    def obtain_users_by_id(self,id):
        '''Fill your code here'''
        dbObj = DBConnection()
        mydb = dbObj.get_connection()
        mycursor = mydb.cursor()
        query = "SELECT id FROM user WHERE id= " + str(id)
        mycursor.execute(query)
        result = mycursor.fetchall()
        if len(result) == 0:
            return None
        return result[0][0]
