import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor()
# for multiple inserts use this below line multiple times with the values you want
# mycursor.execute("select * from test2.test_table;")

# selecting specific columns
mycursor.execute("select c1,c5 from test2.test_table;")

# to view the inserted values we use 
for i in mycursor.fetchall():
    print(i)
mydb.close()