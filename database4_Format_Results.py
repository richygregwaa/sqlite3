# FORMAT RESULTS
import sqlite3

# Connect to a database
conn = sqlite3.connect('customer.db') 

# Create a cursor
c = conn.cursor()

# QUERY THE DATABASE

c.execute("SELECT * FROM customers")
# c.fetchone()
# c.fetchmany(3)
# c.fetchall()

# print(c.fetchone())		# (u'John', u'Elder', u'john@codemy.com')
# print (c.fetchmany(3))	# [(u'John', u'Elder', u'john@codemy.com'), (u'Tim', u'Smith', u'tim@codemy.com'), (u'Mary', u'Brown', u'mary@codemy.com')]
# print(c.fetchall())
# print(c.fetchone()[0])		# John


items = (c.fetchall())
for item in items:
	print(item)

	# OUTPUT
		# (u'John', u'Elder', u'john@codemy.com')
		# (u'Tim', u'Smith', u'tim@codemy.com')
		# (u'Mary', u'Brown', u'mary@codemy.com')
		# (u'Wes', u'Brown', u'wes@brown.com')
		# (u'Steph', u'Kuewa', u'steph@kuewa.com')
		# (u'Dan', u'Pas', u'dan@pas.com')

for item in items:
	print(item[0])

	# OUTPUT
		# John
		# Tim
		# Mary
		# Wes
		# Steph
		# Dan

print("NAME " + "\t\tEMAIL")
print("-------" + "\t\t--------")
for item in items:
	print(item[0] + " " + item[1] + "\t" + item[2])		# \t is a tab

	# OUTPUT
		# John Elder	john@codemy.com
		# Tim Smith		tim@codemy.com
		# Mary Brown	mary@codemy.com
		# Wes Brown		wes@brown.com
		# Steph Kuewa	steph@kuewa.com
		# Dan Pas		dan@pas.com


# Commit our command
conn.commit()

# Close our connection
conn.close()

