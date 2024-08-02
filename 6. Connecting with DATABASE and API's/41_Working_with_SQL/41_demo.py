import mysql.connector
# import mysql.connector
#create user 'user'@'%' identified by 'password'
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
print(mydb)
mycursor = mydb.cursor() # cursor ek pointer hai jo create hoga jo one by one data ko padega
mycursor.execute("SHOW DATABASES")
for x in mycursor:
  print(x)