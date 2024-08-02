import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor()
# we uses above line always as using these we are connecting always
mycursor.execute("CREATE DATABASE if not exists test2")
mydb.close()