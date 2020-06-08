import sqlite3

#conn = sqlite3.connect(':memory') 
# This is something you can use if you wanted small db in memory but be aware its gone once computer is switched off

conn = sqlite3.connect('customer.db') 
# By going in macs terminal and changing directory (cd) to  richygregwaa/SublimeProjects/sqlite3/  
# and typing 'python database' the file customer.db was created due to the connect above.

#Create a cursor
c = conn.cursor()



# Create a Table - Note when I'm keying in several lines it's best to use doc strings """
# This was run once from the terminal and then on course below was deleted

c.execute(""" CREATE TABLE customers (
		first_name text,
		last_name text,
		email text
	)""")


# This line below would also work as above but could become very long on more complex lines
# c.execute("CREATE TABLE customers (first_name DATATYPE,last_name DATATYPE,email DATATYPE))


#Types of string in sqlite types. Good thing is there are only 5 or 6 which helps keep things simple. DBs such as MySql might have about 12
# Datatypes
# NULL
# INTEGER
# REAL
# TEXT
# BLOB

# Commit our command
conn.commit()

# Close our connection
conn.close()

