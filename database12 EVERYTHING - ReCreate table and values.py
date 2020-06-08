#11 Everything - ReCreate table and values


import sqlite3

# Connect to a database
conn = sqlite3.connect('customer.db') 

# Create a cursor
c = conn.cursor()



c.execute(""" CREATE TABLE customers (
		first_name text,
		last_name text,
		email text
	)""")



# INSERTING MANY RECORDS AT A TIME

many_customers = [

					('Wes', 'Brown', 'wes@brown.com'),
					('Steph','Kuewa','steph@kuewa.com'),
					('Dan', 'Pas', 'dan@pas.com'),
					('John', 'Elder','john@codemy.com'),
					('Tim', 'Smith','tim@codemy.com'),
					('Mary', 'Brown','mary@codemy.com'),

					]

c.executemany("INSERT INTO customers VALUES (?,?,?)",many_customers)


c.execute("SELECT * FROM customers")

items = (c.fetchall())
for item in items:
	print(item)


# Commit our command
conn.commit()

# Close our connection
conn.close()
