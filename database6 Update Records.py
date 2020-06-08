# Update Records

import sqlite3

# Connect to a database
conn = sqlite3.connect('customer.db') 

# Create a cursor
c = conn.cursor()

# Update Records

# c.execute("""UPDATE customers SET first_name = "Bob"
# 			WHERE last_name = 'Elder' 
# 	""")

# c.execute("""UPDATE customers SET first_name = "John"
# 			WHERE rowid = 1 
# 	""")

# c.execute("""UPDATE customers SET first_name = "Marty"
# 			WHERE last_name = 'Brown' 
# 	""")

# c.execute("""UPDATE customers SET first_name = "Mary"
# 			WHERE last_name = 'Brown' 
# 	""")

c.execute("""UPDATE customers SET first_name = "Wes"
			WHERE rowid = 4 
	""")



# Commit our command
conn.commit()




# QUERY THE DATABASE
c.execute("SELECT rowid, * FROM customers")

items = (c.fetchall())

for item in items:
	print(item)



# Close our connection
conn.close()

