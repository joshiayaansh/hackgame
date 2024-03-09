import sqlite3 

print("Welcome to the hacking terminal portal!")
print("setting you up... ready!")
name = input("Enter user name:")
password = input("Enter a password to keep your account safe:")
login = input("Enter your login:")
  # Assign the input to a variable
if login == (name + " " + password):
    print("Successful login.")
elif login == name:
    print("You only entered the username. Please enter username and password.")
elif login == password: 
    print("You only entered the password. Please enter username and password.")
else: 
    print("Unsuccessful login.")

# Connect to SQLite database in memory
conn = sqlite3.connect(':memory:')

# Create a cursor
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE users
             (username text, password text)''')

# Insert a row of data
c.execute("INSERT INTO users VALUES (?, ?)", (name, password))

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
class System:
    password = ("8y573yf")
    password2 = ("querty123")
    password3 = ("avf325f")
print("Oh no! Hackers are trying to get into your system and have locked your computer! Guess the passwords for all three systems to win!")

passwordguess = input("")