Python is a high-level, object-oriented programming language that is easy to learn and use. With Python, developers can create powerful applications in a short amount of time. In this article, we will discuss how to perform CRUD operations with MySQL using Python. The github link is below

Download and Install MySQL Connector for Python Mysql CRUD example

The first step to using MySQL with Python is to download and install the MySQL Connector. Before installing, make sure that you have installed Python on your machine. Here's how you can install the connector using pip:

pythonCopy code python -m pip install mysql-connector-python

Test MySQL Connector

To test if the installation was successful, create a Python page with the following content:

pythonCopy codeimport mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="finalproje2db"
)

print(mydb)

Python MySQL Database Creation for Python Mysql CRUD example

To create a database in MySQL, use the "CREATE DATABASE" statement:

pythonCopy codemycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE finalproje2")

Python MySQL Table Creation

To create a table in MySQL, use the "CREATE TABLE" statement. Make sure to define the name of the database when creating the connection:

pythonCopy codemycursor = mydb.cursor()
mycursor.execute("CREATE TABLE finaltablo (name VARCHAR(255), address VARCHAR(255))")

Inserting Data Into Table for Python Mysql CRUD example

To insert data into a table in MySQL, use the "INSERT INTO" statement:

pythonCopy codemycursor = mydb.cursor()
sql = "INSERT INTO kitaplik (id, KitapAd, Yazar) VALUES (%s, %s, %s)"
val = (55, "Cendere Cendere", "Selin Cantuğ")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")

To insert multiple rows at once, use the "executemany" method:

pythonCopy codesql = "INSERT INTO kitaplik (id, KitapAd, Yazar) VALUES (%s, %s, %s)"
val = [
  ('KitapAdı1', 'engin karatas'),
  ('Metametarials', 'mehmet bakır'),
]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "rows were inserted.")

Selecting Data From Table

To select data from a table in MySQL, use the "SELECT" statement:

pythonCopy codemycursor = mydb.cursor()
mycursor.execute("SELECT * FROM kitaplik")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

To select the first record that matches a specific condition, use the "fetchone" method:

pythonCopy codemycursor = mydb.cursor()
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchone()
print(myresult)

Deleting Data From Table

To delete data from an existing table, use the "DELETE FROM" statement:

pythonCopy codemycursor = mydb.cursor()
sql = "DELETE FROM kitaplik WHERE id = 55"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) deleted")

Updating Data in Table

To update a record in a table, use the "UPDATE" statement:

pythonCopy codemycursor = mydb.cursor()
sql = "UPDATE kitaplik SET Yazar = 'Engin Karatas' WHERE id = 55"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s)

explanation link:👉 https://enginkaratas.com/python-crud-opreations/
