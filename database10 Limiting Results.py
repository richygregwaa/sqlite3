#10 Limiting Results

import sqlite3

# Connect to a database
conn = sqlite3.connect('customer.db') 

# Create a cursor
c = conn.cursor()


# Query The Database - LIMITING RESULTS
# c.execute("SELECT rowid, * FROM customers LIMIT 2");
	# (1, u'John', u'Elder', u'john@codemy.com')
	# (2, u'Tim', u'Smith', u'tim@codemy.com')

# LIMIT2 needs to be at the end
c.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC LIMIT 2");
	# (5, u'Steph', u'Kuewa', u'steph@kuewa.com')
	# (4, u'Wes', u'Brown', u'wes@brown.com')


items = (c.fetchall())

for item in items:
	print(item)



# Commit our command
conn.commit()


# Close our connection
conn.close()
