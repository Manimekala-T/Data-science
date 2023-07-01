import mysql.connector
# import mysql.connector
#create user 'user'@'%' identified by 'password'
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor()
mycursor.execute("insert into newdb.table1(c1) values(45)")
#mycursor.execute("update newdb.table1 set c1=90")
#mycursor.execute("delete from newdb.table1")
mydb.commit()
mydb.close()

#Q3. What is DML? Explain INSERT, UPDATE, and DELETE with an example.