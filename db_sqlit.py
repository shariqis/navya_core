import sqlite3

conn = sqlite3.connect('anu.db')
# # # print ("Opened database successfully")
# # # # # ####

# conn.execute('''CREATE TABLE COMPANY1
#          (ID INT PRIMARY KEY     NOT NULL,
#          NAME           TEXT    NOT NULL,
#          AGE            INT     NOT NULL,
#          ADDRESS        CHAR(50),
#          SALARY         REAL)''')
# # # print ("Table created successfully")


# # # # # # # ##########


# conn.execute("INSERT INTO COMPANY1 (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (2, 'anu', 32, 'india', 20000.00 )")

# conn.execute("INSERT INTO COMPANY1 (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (6, 'aa', 32, 'india', 20000.00 )")

# conn.commit()
# print ("Total number of rows updated :", conn.total_changes)
# # # print ("Records created successfully")     


# # # # # # # ####################


v = conn.execute("SELECT id, name, address, salary from COMPANY1")
print(v)
# # # print('------------------')
for row in v:
   print(row)
# # #    print(type(row))
# # #    print ("ID = ", row[0])
# # #    print ("NAME = ", row[1])
# # #    print ("ADDRESS = ", row[2])
# # #    print ("SALARY = ", row[3], "\n")
# # #    print('------------------')   

# # # print ("Operation done successfully")


# # # # # # ###########


# # # conn.execute("UPDATE COMPANY set SALARY = 25000.00 where ID = 4")
# # # conn.commit()

# # # print ("Total number of rows updated :", conn.total_changes)
# # # print('.......................')
# # # cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
# # # for row in cursor:
# # #    print ("ID = ", row[0])
# # #    print ("NAME = ", row[1])
# # #    print ("ADDRESS = ", row[2])
# # #    print ("SALARY = ", row[3], "\n")
# # # print ("Total number of rows updated :", conn.total_changes)
# # # print ("Operation done successfully")

# # # conn.close()