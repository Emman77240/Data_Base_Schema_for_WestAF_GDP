#!/usr/bin/python

import mysql.connector as mariadb
"""
mariadb_connection = mariadb.connect(host='localhost', user='root', password='godman')

cursor = mariadb_connection.cursor()

cursor.execute("CREATE DATABASE myGDPdata")
mariadb_connection.commit()

comment out the above code after creating the database"""

mariadb_connection = mariadb.connect(host='localhost', user='root', password='godman', database='myGDPdata')

cursor = mariadb_connection.cursor()

cursor.execute("CREATE TABLE country_info (CountryID INT NOT NULL PRIMARY KEY AUTO_INCREMENT, CountryName VARCHAR(100) NOT NULL,SizeSQKM INT, DollarGDP INT)")

cursor.execute("CREATE TABLE country_size (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, Population INT)")


sql = "INSERT INTO country_info (CountryName,SizeSQKM,DollarGDP) VALUES (%s, %s, %s)"
val = [
  ('Benin', '114763', '9274000'),
  ('Ghana', '238535', '47330000'),
  ('Nigeria', '923768', '375771000')
]

cursor.executemany(sql, val)

mariadb_connection.commit()