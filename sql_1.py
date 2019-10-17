import mysql.connector
mydb = mysql.connector.connect(
    host = 'localhost',
    user='root',
    password = 'sanyam1996',
    database = 'db1')
print(mydb.connection_id)
cur = mydb.cursor()
s = 'insert into book (bookid,title,price) values(%s,%s,%S)'
b1 = (1,'python3',345)
cur.execute(s,b1)
mydb.commit()