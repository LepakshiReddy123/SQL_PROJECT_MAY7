"""In the “sale” table, it should include all the items got sold
 in different stores with the sale date, profit margin, etc"""


#importing required libraries
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Lep@kshi123@",
    database = "Inventory_Management"# using the created database
)
mycursor = mydb.cursor()
#creating table sale
mycursor.execute("CREATE TABLE sale(\
                 sale_id INT NOT NULL,\
                 store_name VARCHAR(30),\
                 product_name VARCHAR(30) NOT NULL,\
                 sale_date DATE NOT NULL,\
                 profit_margin DECIMAL(8,2),\
                 PRIMARY KEY(sale_id),\
                 FOREIGN KEY (product_name) REFERENCES manufacture(product_name))")
#checking existing tables in the database Inventory_Management
mycursor.execute("show tables")
for i in mycursor:
    print(i)
#Inserting data into the sale table
key ="INSERT INTO sale(sale_id,store_name,product_name,sale_date,profit_margin) VALUES(%s , %s, %s, %s,%s)"
value = [
    (1,"MY Care","Wooden Table","2023-5-7",500),
    (2,"My kids","Red Toy","2023-5-8",100),
    (3,"Wood","Door","2023-5-2",500),
    (4,"ORAY","Wooden Toys","2023-5-5",20)
]
# usind executemany() to execute all the input at a time
mycursor.executemany(key,value)
mydb.commit()
#displaying all the entries in the sale table
result = "SELECT * FROM sale"
mycursor.execute(result)
display = mycursor.fetchall()#used to fetch all the entries in the table 
for i in display:
    print(i)


