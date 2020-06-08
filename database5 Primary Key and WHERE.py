# 5 Primary Key and WHERE

import sqlite3

# Connect to a database
conn = sqlite3.connect('customer.db') 

# Create a cursor
c = conn.cursor()

# QUERY THE DATABASE

# c.execute("SELECT rowid, * FROM customers WHERE last_name = 'Elder'")
# c.execute("SELECT rowid, * FROM customers WHERE last_name <= 'Elder'")
# c.execute("SELECT rowid, * FROM customers WHERE last_name > 'Elder'")
# c.execute("SELECT rowid, * FROM customers WHERE last_name LIKE 'Br%' ")
c.execute("SELECT rowid, * FROM customers WHERE email LIKE '%codemy.com' ")

items = (c.fetchall())

for item in items:
	print(item)









# Commit our command
conn.commit()

# Close our connection
conn.close()

