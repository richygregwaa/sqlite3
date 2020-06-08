import sqlite3


#Query The Database and Return All Records
def show_all():
	# Connect to a database
	conn = sqlite3.connect('customer.db') 

	# Create a cursor
	c = conn.cursor()

	# Query The Database - OUR APP SHOW ALL FUNCTIONS
	c.execute("SELECT rowid, * FROM customers")
	items = (c.fetchall())

	for item in items:
		print(item)

	# Commit our command
	conn.commit()

	# Close our connection
	conn.close()


# Add A New Record To The Table
def add_one(first,last,email):
	conn = sqlite3.connect('customer.db') 
	c = conn.cursor()
	c.execute("INSERT INTO customers VALUES (?,?,?)",(first,last,email))
	# Commit our command
	conn.commit()
	# Close our connection
	conn.close()


# Add Many Records To Table
def add_many(list):
	conn = sqlite3.connect('customer.db') 
	c = conn.cursor()
	c.executemany("INSERT INTO customers VALUES (?,?,?)",(list))
	# Commit our command and Close connection
	conn.commit()
	conn.close()



# Delete Record from table
def delete_one(id):
	conn = sqlite3.connect('customer.db') 
	c = conn.cursor()
	c.execute("DELETE from customers WHERE rowid = (?)",id)	
	conn.commit()
	# Close our connection
	conn.close()


# Lookup with Where
def email_lookup(email):
	conn = sqlite3.connect('customer.db') 
	c = conn.cursor()
	c.execute("SELECT rowid, * from customers WHERE email = (?)",(email,))
	items = (c.fetchall())

	for item in items:
		print(item)


	conn.commit()
	# Close our connection
	conn.close()









