import sqlite3

# Connect to a database
conn = sqlite3.connect('customer.db') 

# Create a cursor
c = conn.cursor()

# INSERTING MANY RECORDS AT A TIME

many_customers = [

					('Wes', 'Brown', 'wes@brown.com'),
					('Steph','Kuewa','steph@kuewa.com'),
					('Dan', 'Pas', 'dan@pas.com'),
					]



c.executemany("INSERT INTO customers VALUES (?,?,?)",many_customers)



print("Command executed successfully")
# Commit our command
conn.commit()

# Close our connection
conn.close()

