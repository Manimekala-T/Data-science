import mysql.connector
# import mysql.connector
#create user 'user'@'%' identified by 'password'
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor()
#mycursor.execute("drop table newdb.table2")
#mycursor.execute("truncate table newdb.table1")
mycursor.execute("ALTER TABLE newdb.table1 add COLUMN (c2 int)")
mydb.close()

#comment the query which is not needed and run the necessary ones
'''Q3.The SQL commands that deal with the manipulation of data present in the database belong to DML or Data Manipulation Language and this includes most of the SQL statements.
INSERT: It is used to insert data into a table.
UPDATE: It is used to update existing data within a table.
DELETE: It is used to delete records from a database table.'''
