#importing library
import mysql.connector

#Creating a connection with the server
mydb = mysql.connector.connect(host = '127.0.0.1', user = 'root', password = 'Akshu@2001',database='esm1')

print(mydb) #To check whether the connection was successful

#creating cursor
mycursor = mydb.cursor()

# creating database
##create_db = "CREATE DATABASE esm1"
##mycursor.execute(create_db)

# creating a table
##create_table = """CREATE TABLE product_info (Product_id INT Primary key,Product_type VARCHAR(225),Product_brand VARCHAR(225),Product_model VARCHAR(225),Product_MRP INT,Product_CP INT)"""
##
##mycursor.execute(create_table)
##
##create_table = """CREATE TABLE customer_info (
##     Customer_id INT ,
##     Customer_name VARCHAR(225),
##     Customer_contact VARCHAR(500) Primary key,
##     Customer_gender VARCHAR(225),
##     Customer_location VARCHAR(225),
##     Customer_age INT
## )"""
##
##mycursor.execute(create_table)
##
##create_table = """CREATE TABLE sales_info (
##     Invoice_id INT,
##     Item_number INT,
##     Date DATE,
##     Customer_contact VARCHAR(500),
##     Customer_name VARCHAR(500),
##     Product_id INT,
##     Quantity INT,
##     MRP INT,
##     Discount INT,
##     Actual_Sale_Price INT,
##     CONSTRAINT PK_Sales_info PRIMARY KEY (Invoice_id,Item_number),
##     FOREIGN KEY (Customer_contact) REFERENCES customer_info(Customer_contact),
##     FOREIGN KEY (Product_id) REFERENCES product_info(Product_id)
## )"""
##
##mycursor.execute(create_table)
##
##create_table = """CREATE TABLE admin (
##     Employee_id INT  PRIMARY KEY,
##     Employee_name VARCHAR(500),
##     Employee_contact VARCHAR(500),
##     Employee_gender VARCHAR(2),
##     Employee_age INT
##     )"""
##
##mycursor.execute(create_table)
##
##
####for login window
####create_table = """CREATE TABLE LOGIN (
####    username VARCHAR(50),
####    password VARCHAR(50)
####     )"""
####
####mycursor.execute(create_table)
##
####For Product table to insert values
def items_values(val):
    query = """INSERT INTO product_info(Product_id,Product_type,Product_brand,Product_model,Product_MRP,Product_CP)
    VALUES(%s,%s,%s,%s,%s,%s) """
    mycursor.execute(query,val)
    mydb.commit()
    
####For Customer table to insert values
def customer_values(val):
    query = """INSERT INTO customer_info(Customer_id,Customer_name,Customer_contact,Customer_gender,Customer_location,Customer_age)
    VALUES(%s,%s,%s,%s,%s,%s) """
    mycursor.execute(query,val)
    mydb.commit()
    
####For Admin table to insert values    
def admin_values(val): 
    query = """INSERT INTO admin(Employee_id,Employee_name,Employee_contact,Employee_gender,Employee_age)
    VALUES(%s,%s,%s,%s,%s) """
    mycursor.execute(query,val)
    mydb.commit()
    
####For Sales table to insert values
def sales_values(val):   
    query = """INSERT INTO sales_info(Invoice_id,Item_number,Date,Customer_id,Product_id,Quantity,MRP,Discount,Actual_Sale_Price)
    VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s) """
    mycursor.execute(query,val)
    mydb.commit()

####For Customer table to fetch values
def get_customer():
    query = """SELECT * FROM customer_info"""
    mycursor.execute(query)
    result = mycursor.fetchall()
    return result

####For Product table to fetch values
def get_item():
    query = """SELECT * FROM product_info"""
    mycursor.execute(query)
    result = mycursor.fetchall()
    return result

####For Admin table to fetch values
def get_employee():
    query = """SELECT * FROM admin"""
    mycursor.execute(query)
    result = mycursor.fetchall()
    return result

####For Customer table to display values    
def display_customer_info(val):
    query ="""Select Customer_id,Customer_name,Customer_gender,Customer_location,Customer_age FROM customer_info WHERE Customer_contact = %s """
    mycursor.execute(query,val)
    result = mycursor.fetchone()
    return result

####For Customer table to update values
def customer_update(val):
    query = """UPDATE customer_info SET Customer_id=%s,Customer_name=%s,Customer_gender=%s,Customer_location=%s,Customer_age = %s WHERE Customer_contact = %s """
    mycursor.execute(query,val)
    mydb.commit()

####For Products table to display values    
def display_items_info(val):
    query ="""Select Product_type,Product_brand,Product_model,Product_MRP,Product_CP FROM product_info WHERE Product_id = %s """
    mycursor.execute(query,val)
    result = mycursor.fetchone()
    return result

####For Product table to update values   
def item_update(val): 
    query = """UPDATE product_info set Product_type = %s,Product_brand = %s,Product_model = %s,Product_MRP = %s,Product_CP = %s WHERE Product_id = %s"""
    mycursor.execute(query,val)
    mydb.commit()

####For Admin table to display values    
def display_employee_info(val):
    query ="""Select Employee_name,Employee_contact,Employee_gender,Employee_age FROM admin WHERE Employee_id = %s """
    mycursor.execute(query,val)
    result = mycursor.fetchone()
    return result

####For Admin table to update values   
def admin_update(val): 
    query = """UPDATE admin set Employee_name = %s,Employee_contact = %s,Employee_gender = %s,Employee_age = %s WHERE Employee_id = %s"""
    mycursor.execute(query,val)
    mydb.commit()

####For Product table to delete values
def delete_item(val):
    query = """DELETE FROM product_info WHERE Product_id = %s"""
    mycursor.execute(query,val)
    mydb.commit()

####For Admin table to delete values    
def delete_admin(val):
    query = """DELETE FROM admin WHERE Employee_id = %s"""
    mycursor.execute(query,val)
    mydb.commit()

####For Customer table to delete values   
def delete_customer(val):
    query = """DELETE FROM customer_info WHERE Customer_contact = %s"""
    mycursor.execute(query,val)
    mydb.commit()

####For Sales table to display values    
def display_invoice_info(val):
    query ="""Select Item_number,Date,Customer_contact,Customer_name,Product_id,Quantity,MRP,Discount,Actual_Sale_Price FROM sales_info WHERE Invoice_id = %s and Item_number = %s"""
    mycursor.execute(query,val)
    result = mycursor.fetchone()
    return result

####For Product table to select values
def selected_items():
    query ="""SELECT Product_id,Product_brand,Product_model,Product_MRP FROM product_info"""
    mycursor.execute(query)
    result = mycursor.fetchall()
    return result

####For Product table to insert values into cart  
def add_cart_items(val):
    query ="""SELECT Product_brand,Product_model,Product_MRP FROM product_info WHERE Product_id = %s"""
    mycursor.execute(query,val)
    result = mycursor.fetchone()
    return result 

####For Product table to search values    
def Product_search(val):
    query = """SELECT Product_id,Product_brand,Product_model,Product_MRP FROM product_info WHERE Product_brand = %s """ 
    mycursor.execute(query,val)
    result = mycursor.fetchall()
    return result
