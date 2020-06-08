# 11 Drop Table


import sqlite3

# Connect to a database
conn = sqlite3.connect('customer.db') 

# Create a cursor
c = conn.cursor()


# Drop Table
c.execute("DROP TABLE customers")
conn.commit()


# Query The Database
c.execute("SELECT rowid, * FROM customers");

	# Traceback (most recent call last):
	#   File "database.py", line 17, in <module>
	#     c.execute("SELECT rowid, * FROM customers");
	# sqlite3.OperationalError: no such table: customers


items = (c.fetchall())

for item in items:
	print(item)



# Commit our command
conn.commit()


# Close our connection
conn.close()
