# DELETE Record

import sqlite3

# Connect to a database
conn = sqlite3.connect('customer.db') 

# Create a cursor
c = conn.cursor()

# DELETE Records
# c.execute("DELETE from customers WHERE rowid > 6")


# c.execute("UPDATE customers SET first_name = 'John' WHERE rowid = 1")




# Commit our command
conn.commit()




# QUERY THE DATABASE
c.execute("SELECT rowid, * FROM customers")

items = (c.fetchall())

for item in items:
	print(item)



# Close our connection
conn.close()

