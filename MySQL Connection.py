
'''
import mysql.connector
myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "admin123",database = "pythonconn")
cur = myconn.cursor()
try:
  dbs = cur.execute("create table Employee(name varchar(20) not null, id int(20) not null primary key, salary float not null, Dept_id int not null)")
except:
    myconn.rollback()
myconn.close()
'''

'''
import mysql.connector
mysql.connector.connect
myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "admin123",database = "pythonconn")
cur = myconn.cursor()
try:
    dbs = cur.execute("create table Employee(name varchar(20) not null, id int(20) not null primary key, salary float not null, Dept_id int not null)")
except:
    myconn.rollback()
myconn.close()
'''

'''
import mysql.connector
myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "admin123",database = "pythonconn")
cur = myconn.cursor()
try:
    cur.execute("alter table Employee add branch_name varchar(20) not null")
except:
    myconn.rollback()
myconn.close()
'''

'''
import mysql.connector
myconn = mysql.connector.connect(host="localhost", user="root", passwd="admin123", database="pythonconn")
cur = myconn.cursor()
sql = "insert into Employee(name, id, salary, dept_id, branch_name) values (%s, %s, %s, %s, %s)"
values = ("John", 110, 25000.00, 201, "Newyork")
try:
    cur.execute(sql, values)
    myconn.commit()
except:
    myconn.rollback()
print(cur.rowcount, "record inserted!")
myconn.close()  
'''

'''
import mysql.connector
myconn = mysql.connector.connect(host="localhost", user="root", passwd="admin123", database="pythonconn")
cur = myconn.cursor()
sql = "insert into Employee(name, id, salary, dept_id, branch_name) values ("Tom", 220, 50000.00, 501, "DC")"
try:
    cur.execute(sql)
    myconn.commit()
except:
    myconn.rollback()
print(cur.rowcount, "record inserted!")
myconn.close()  
'''

'''
import mysql.connector

myconn = mysql.connector.connect(host="localhost", user="root", passwd="admin123", database="pythonconn")
cur = myconn.cursor()
sql = "insert into Employee(name, id, salary, dept_id, branch_name) values (%s, %s, %s, %s, %s)"
val = [("John", 102, 25000.00, 201, "Newyork"), ("David", 103, 25000.00, 202, "Port of spain"),
       ("Nick", 104, 90000.00, 201, "Newyork")]
try:
    cur.executemany(sql, val)
    myconn.commit()
    print(cur.rowcount, "records inserted!")
except:
    myconn.rollback()
myconn.close()
'''

'''
import mysql.connector
myconn=mysql.connector.connect(host="localhost",user="root",passwd="admin123",database="pythonconn")
cur=myconn.cursor()
sql = "insert into store(id,location,distance) values (10,'thailand','5km')"
try:
    cur.execute(sql)
    myconn.commit()
    print(cur.rowcount, "record inserted! id:", cur.lastrowid)
except:
    myconn.rollback()
myconn.close()
'''


'''
import mysql.connector
myconn = mysql.connector.connect(host="localhost", user="root", passwd="admin123", database="pythonconn")
cur = myconn.cursor()
try:
    cur.execute("select * from books")
    result = cur.fetchall()
    for x in result:
        print(x);
except:
    myconn.rollback()
myconn.close()
'''

'''
import mysql.connector
myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "admin123",database = "pythonconn")
cur = myconn.cursor()
try:
    cur.execute("select id, name, price from books where name='ttt'")
    result = cur.fetchone()
    print(result)
except:
    myconn.rollback()
myconn.close()
'''

'''
import mysql.connector
myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "admin123",database = "pythonconn")
cur = myconn.cursor()
try:
    cur.execute("select  id,name,price from books")
    result = cur.fetchall()
    print("id    Name   Salary")
    for row in result:

        print("%d   %s   %d" %(row[0],row[1],row[2]))
except:
    myconn.rollback()
myconn.close()
'''

'''
import mysql.connector
myconn = mysql.connector.connect(host="localhost", user="root", passwd="admin123", database="pythonconn")
cur = myconn.cursor()
try:
    cur.execute("select books.id, books.name, books.price, store.location, store.distance from store join books on store.id = books.id GROUP BY books.name Desc")
    print("id    name    price   location    distance")
    for row in cur:
        print("%d    %s    %d    %s    %d" %(row[0], row[1], row[2], row[3], row[4]))
except:
    myconn.rollback()
myconn.close()
'''

'''
import mysql.connector
myconn=mysql.connector.connect(host="localhost", user="root", passwd="admin123", database="pythonconn")
cur=myconn.cursor()
rowcount=0
try:
    cur.execute("delete from Employee where id between 200 to 400")
    myconn.commit()
    print(cur.rowcount, "row delete, id:", cur.lastrowid)
except:
    print("cannot be deleted")
    myconn.rollback()
myconn.close()
'''

'''
import mysql.connector
myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "admin123",database = "pythonconn")
cur = myconn.cursor()
try:
    cur.execute("UPDATE books SET price= 6700 WHERE id = 12")
    myconn.commit()
except:
    myconn.rollback()
myconn.close()
'''



