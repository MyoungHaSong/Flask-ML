import mysql
import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '0000',
    database = 'my_rest_db'
)
cursor = mydb.cursor()
cursor.execute(
    'CREATE TABLE svhn (id CHAR(10) PRIMARY KEY,label CHAR(1),path CHAR(60))')
cursor.execute('SHOW TABLES')
for x in cursor:
    print(x)