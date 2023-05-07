"""In the “manufacture” table, one should be able to see all the products that need to be manufactured,
and defective items during the manufacture with different entries like manufacture id, number of items required, etc."""



#importing required libraries
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Lep@kshi123@",
    database = "Inventory_Management"# using the created database
)
mycursor = mydb.cursor()
#creating table manufacture here i am considering product_name  as a PRIMARY KEY to use it in other tables using FOREIGN KEY
mycursor.execute("CREATE TABLE manufacture (\
                 manufacture_id INT NOT NULL,\
                 manufacture_company VARCHAR(30) NOT NULL,\
                 product_name VARCHAR(30) PRIMARY KEY NOT NULL,\
                 no_of_items INT NOT NULL,\
                 defective_items INT,\
                 UNIQUE(manufacture_id))")
#checking existing tables in the database Inventory_Management
mycursor.execute("show tables")
for i in mycursor:
    print(i)
#Inserting data into the manufacture table
key ="INSERT INTO manufacture (manufacture_id,manufacture_company,product_name,no_of_items,defective_items)\
      VALUES(%s , %s, %s, %s, %s)"
value = [
    (1,"SS EXPORT","Wooden Table",20,1),
    (2,"RR EXPORT","Red Toy",15,0),
    (3,"SS EXPORT","Door",4,0),
    (4,"RR EXPORT","Wooden Toys",8,1),
    (5,"RR EXPORT","Wooden Chair",8,1)
]
mycursor.executemany(key,value)
mydb.commit()
#displaying all the entries in the manufacture table
result = "SELECT * FROM manufacture"
mycursor.execute(result)
display = mycursor.fetchall()#used to fetch all the entries in the table 
for i in display:
    print(i)






