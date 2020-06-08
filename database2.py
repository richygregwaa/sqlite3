import sqlite3

# Connect to a database
conn = sqlite3.connect('customer.db') 

# Create a cursor
c = conn.cursor()

# INSERTING ONE RECORD AT A TIME

# c.execute("INSERT INTO customers VALUES ('John', 'Elder','john@codemy.com')")
# c.execute("INSERT INTO customers VALUES ('Tim', 'Smith','tim@codemy.com')")
c.execute("INSERT INTO customers VALUES ('Mary', 'Brown','mary@codemy.com')")



print("Command executed successfully")
# Commit our command
conn.commit()

# Close our connection
conn.close()

