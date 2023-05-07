#Create a database called “Inventory_Management” with different tables like “manufacture”, “goods”, “purchase”, “sale” etc.
# importing required libraries
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Lep@kshi123@"
)
print(mydb)
#preparing a cursor object
mycursor = mydb.cursor()
#creating database
mycursor.execute("CREATE DATABASE Inventory_Management")
#list out all the existing databases
mycursor.execute("SHOW DATABASES")
for i in mycursor:
    print(i)
mydb.close()
