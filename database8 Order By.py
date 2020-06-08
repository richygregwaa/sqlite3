# 8 Order Results By

import sqlite3

# Connect to a database
conn = sqlite3.connect('customer.db') 

# Create a cursor
c = conn.cursor()

# ORDER Results





# Query The Database - ORDER BY
# c.execute("SELECT rowid, * FROM customers ORDER BY rowid")
# c.execute("SELECT rowid, * FROM customers ORDER BY rowid ASC")	#ASCending - In this case not needed as it is the default anyway
#c.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC")	#DESCending

	# (5, u'Steph', u'Kuewa', u'steph@kuewa.com')
	# (4, u'Wes', u'Brown', u'wes@brown.com')
	# (3, u'Mary', u'Brown', u'mary@codemy.com')
	# (2, u'Tim', u'Smith', u'tim@codemy.com')
	# (1, u'John', u'Elder', u'john@codemy.com')

c.execute("SELECT rowid, * FROM customers ORDER BY last_name")

	# (3, u'Mary', u'Brown', u'mary@codemy.com')
	# (4, u'Wes', u'Brown', u'wes@brown.com')
	# (1, u'John', u'Elder', u'john@codemy.com')
	# (5, u'Steph', u'Kuewa', u'steph@kuewa.com')
	# (2, u'Tim', u'Smith', u'tim@codemy.com')

c.execute("SELECT rowid, * FROM customers ORDER BY last_name DESC")

	# (2, u'Tim', u'Smith', u'tim@codemy.com')
	# (5, u'Steph', u'Kuewa', u'steph@kuewa.com')
	# (1, u'John', u'Elder', u'john@codemy.com')
	# (3, u'Mary', u'Brown', u'mary@codemy.com')
	# (4, u'Wes', u'Brown', u'wes@brown.com')
	


items = (c.fetchall())

for item in items:
	print(item)



# Commit our command
conn.commit()


# Close our connection
conn.close()

