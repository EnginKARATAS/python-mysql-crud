 
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="finalproje2db"
)

# print(mydb) #çıktı : <mysql.connector.connection.MySQLConnection object at 0x000001B7F64B5BB0>

##create db 
# mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE xxxxx")

#create table
# mycursor = mydb.cursor()

# mycursor.execute("create table kitaplikPy(id int, KitapAd varchar(40), Yazar varchar(40))")




##insert into table

# mycursor = mydb.cursor()

# sql = "INSERT INTO kitaplik (id,KitapAd, Yazar) VALUES (%s,%s,%s)"
# val = (55,"Cendere Cendere", "Selin Cantuğ")
# mycursor.execute(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "record inserted.")



##multiple column instert 
# sql = "INSERT INTO kitaplik (id,KitapAd, Yazar) VALUES (%s,%s,%s)"
# val = [
#   ('Peter', 'Lowstreet 4'),
#   ('Amy', 'Apple st 652'),
#   ('Hannah', 'Mountain 21'),
#   ('Michael', 'Valley 345'),
#   ('Sandy', 'Ocean blvd 2'),
#   ('Betty', 'Green Grass 1'),
#   ('Richard', 'Sky st 331'),
#   ('Susan', 'One way 98'),
#   ('Vicky', 'Yellow Garden 2'),
#   ('Ben', 'Park Lane 38'),
#   ('William', 'Central st 954'),
#   ('Chuck', 'Main Road 989'),
#   ('Viola', 'Sideway 1633')
# ]

# mycursor.executemany(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "was inserted.")



##select table

# mycursor = mydb.cursor()

# mycursor.execute("SELECT * FROM kitaplik ")

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)

##fetch one

# mycursor = mydb.cursor()

# mycursor.execute("SELECT * FROM kitaplik")

# myresult = mycursor.fetchone()

# print(myresult)


## delete statement 

# mycursor = mydb.cursor()

# sql = "DELETE FROM kitaplik WHERE id = 55"

# mycursor.execute(sql)

# mydb.commit()

# print(mycursor.rowcount, "record(s) deleted")

## update record 

mycursor = mydb.cursor()

sql = "UPDATE kitaplik SET KitapAd = 'XXX' WHERE id = 4"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")

