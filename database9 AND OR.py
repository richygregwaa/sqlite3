#9 AND OR


import sqlite3

# Connect to a database
conn = sqlite3.connect('customer.db') 

# Create a cursor
c = conn.cursor()

# AND/OR


# Query The Database - AND/OR
# c.execute("SELECT rowid, * FROM customers WHERE last_name LIKE 'Br%' AND rowid = 3")

#c.execute("SELECT rowid, * FROM customers WHERE last_name LIKE 'Br%' AND rowid = 3")
	#(3, u'Mary', u'Brown', u'mary@codemy.com')

#c.execute("SELECT rowid, * FROM customers WHERE last_name LIKE 'Br%' OR rowid = 3")
	# (3, u'Mary', u'Brown', u'mary@codemy.com')
	# (4, u'Wes', u'Brown', u'wes@brown.com')

c.execute("SELECT rowid, * FROM customers WHERE last_name LIKE 'Br%' OR rowid = 3 OR email LIKE '%emy.com'")	#You can have as many AND ORS as you like
	# (1, u'John', u'Elder', u'john@codemy.com')
	# (2, u'Tim', u'Smith', u'tim@codemy.com')
	# (3, u'Mary', u'Brown', u'mary@codemy.com')
	# (4, u'Wes', u'Brown', u'wes@brown.com')




items = (c.fetchall())

for item in items:
	print(item)



# Commit our command
conn.commit()


# Close our connection
conn.close()
