"""In the “purchase” table, it should include all the purchase details that are purchased in different online 
and offline stores, along with the purchase id, purchase amount, etc."""


#importing required libraries
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Lep@kshi123@",
    database = "Inventory_Management"# using the created database
)
mycursor = mydb.cursor()
#creating table purchase
mycursor.execute("CREATE TABLE purchase(\
                 purchase_id INT NOT NULL,\
                 product_name VARCHAR(30) NOT NULL,\
                 purchase_date DATE NOT NULL,\
                 purchase_amount DECIMAL(8,2),\
                 mode_of_payment VARCHAR(30),\
                 PRIMARY KEY(purchase_id),\
                 FOREIGN KEY (product_name) REFERENCES manufacture(product_name))")
#checking existing tables in the database Inventory_Management
mycursor.execute("show tables")
for i in mycursor:
    print(i)
#Inserting data into the purchase table
key ="INSERT INTO purchase(purchase_id,product_name, purchase_date,purchase_amount,mode_of_payment) \
    VALUES(%s , %s, %s, %s, %s)"
value = [
    (1,"Wooden Table","2023-5-5",3000,"OFFLINE"),
    (2,"Red Toy","2023-5-6",500,"ONLINE"),
    (3,"Door","2023-4-30",2500,"OFFLINE"),
    (4,"Wooden Toys","2023-5-1",100,"ONLINE")
]
# usind executemany() to execute all the input at a time
mycursor.executemany(key,value)
mydb.commit()
#displaying all the entries in the purchase table
result = "SELECT * FROM purchase"
mycursor.execute(result)
display = mycursor.fetchall()#used to fetch all the entries in the table 
for i in display:
    print(i)
