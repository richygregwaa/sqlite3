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

print(c.fetchall())


# print("Command executed successfully")
# Commit our command
conn.commit()

# Close our connection
conn.close()
