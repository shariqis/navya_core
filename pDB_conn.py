# python -m pip install mysql-connector-python

import mysql.connector


# # # # # # # # # #    
mydb = mysql.connector.connect(
  host="localhost",
  user="root"  , 
  port=3306,
  # password
  database="navya1"  
)
 
mycursor = mydb.cursor()
# mycursor.execute("SHOW DATABASES")                                                                                    
# # print(mycursor)

# for x in mycursor:
#   print(x)

# mycursor.execute("CREATE DATABASE navya1")
# mydb.commit()


# mycursor.execute("""CREATE TABLE customers (name VARCHAR(255),
# address VARCHAR(255))""")
# mydb.commit()

# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = [  
#   ('nitha', 'Lowstreet 4'),
#   ('mithun', 'Apple st 652'),
#   ('gayathri', 'Mountain 21'),
#   ('aishu', 'Main Road 989'),
#   ('anjith', 'Sideway 1633')
# ]
# mycursor.executemany(sql, val)


# # m= "insert into customers (name, address) VALUES ('shiny','shiny villa') "
# # mycursor.execute(m)
# mydb.commit()

# # # # # # # # # # # -----------------------------------------------------------------


mycursor.execute("SELECT * FROM customers ")

myresult = mycursor.fetchall()

# myresult = mycursor.fetchone()  
print(myresult)

# # # print(type(myresult))

# # # # for x in myresult:
# # # #     # print(x)
# # # # #     print(',,,,,,,,,,,,,,,,,,,,,,,,,,')
# # # #     for i in x:
# # # #         print(i, end= " ")
# # # #     print()    
# # # # # #     print('------------')



# # # # # # # # # # # # myresult = mycursor.fetchone()  