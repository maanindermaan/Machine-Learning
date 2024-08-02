import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor()
# we uses above line always as using these we are connecting always
mycursor.execute("insert into test2.test_table values(123 , 'sudh' , 234.45 , 234 , 'kumar')")
# to make it visible we use commit
mydb.commit()
mydb.close()