# importing required libraries
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Lep@kshi123@",
    database="Inventory_Management"
)
#preparing a cursor object
mycursor = mydb.cursor()
#QUESTION 1:
"""Delete the defective item, e.g., the shirt which was accidentally purchased by the “ORay” store, manufactured on the date ‘01-04-23’."""




#QUESTION 2:
"""Update the manufacture details of all the red-colored toys which are purchased by the “MyKids” store."""




#QUESTION 3:
"""Display all the “wooden chair” items that were manufactured before the 1st May 2023."""

result = " SELECT * FROM manufacture AS m,goods AS g WHERE m.product_name ='Wooden Chair' AND g.product_name=m.product_name AND manufactured_date < '2023-5-1'"
mycursor.execute(result)
display = mycursor.fetchall()
for i in display:
    print(i)





#QUESTION 4:
"""Display the profit margin amount of the “wooden table” that was sold by 
the “MyCare” store, manufactured by the “SS Export” company.

"""

result="SELECT s.profit_margin FROM sale AS s,manufacture AS m \
    WHERE s.product_name=m.product_name AND s.product_name='Wooden Table'AND \
        s.store_name='My Care' AND m.manufacture_company='SS EXPORT'"
mycursor.execute(result)
display = mycursor.fetchall() 
for i in display:
    print(i)
