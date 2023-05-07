"""In the “goods” table, it should include different items that are manufactured
 by the company along with the goods id, manufactured date, etc."""

#importing required libraries
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Lep@kshi123@",
    database = "Inventory_Management"# using the created database
)
mycursor = mydb.cursor()
#creating table goods
mycursor.execute("CREATE TABLE goods(\
                 goods_id INT NOT NULL,\
                 product_name VARCHAR(30) NOT NULL,\
                 manufactured_date DATE NOT NULL,\
                 PRIMARY KEY(goods_id),\
                 FOREIGN KEY (product_name) REFERENCES manufacture(product_name))")
#checking existing tables in the database Inventory_Management
mycursor.execute("show tables")
for i in mycursor:
    print(i)
#Inserting data into the goods table
key ="INSERT INTO goods(goods_id,product_name,manufactured_date) VALUES(%s , %s, %s)"
value = [
    (11,"Red Toy","2023-5-2"),
    (12,"Wooden Table","2023-5-4"),
    (13,"Wooden Toys","2023-4-12"),
    (14,"Door","2023-4-23"),
    (15,"Wooden Chair","2023-4-23")
    
]
# usind executemany() to execute all the input at a time
mycursor.executemany(key,value)
mydb.commit()
#displaying all the entries in the goods table
result = "SELECT * FROM goods"
mycursor.execute(result)
display = mycursor.fetchall()#used to fetch all the entries in the table 
for i in display:
    print(i)

