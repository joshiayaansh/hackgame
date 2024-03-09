import sqlite3 
import sys
import hashlib
icounter = 0
point_counter = 0

def exit_game():
    sys.exit()
def new_point():
    point_counter + 5
def del_point():
    point_counter - 1
print("Welcome to the hacking terminal portal!")
print("setting you up... ready!")
name = input("Enter user name:")
password = input("Enter a password to keep your account safe:")
login = input("Enter your login by using your username space password:")
  # Assign the input to a variable
if login == (name + " " + password):
    print("Successful login.")
elif login == name:
    print("You only entered the username. Please enter username and password.")
elif login == password: 
    print("You only entered the password. Please enter username and password.")
else: 
    print("Unsucessful login.")
    exit_game()

# Connect to SQLite database in a file
conn = sqlite3.connect('name_password.db')

# Create a cursor
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS users
             (username text, password text)''')

hashed_name = hashlib.sha256(name.encode()).hexdigest()
hashed_password = hashlib.sha256(password.encode()).hexdigest()

# Insert a row of data
c.execute("INSERT INTO users VALUES (?, ?)", (hashed_name, hashed_password))

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
passwordguessing = ("minecraft")
password2 = ("querty123")
password3 = (":)")
print("Oh no! Hackers are trying to get into your system and have locked your computer! Guess the passwords for all three systems to win!")
print("Entering system 1...")
print("In!")

while icounter < 3:
    passwordguess = input("Guess the first password: ")
    if passwordguess == (passwordguessing):
        point_counter + 1
        print("Correct!")
        break
    else: 
        icounter = icounter + 1
        print("Incorrect! Hint: it is the name of a popular video game.")

icounter = 0

while icounter < 3:
    passwordguess2 = input("Guess the second password:")
    if passwordguess2 == (password2):
        point_counter + 1
        print("Correct!")
        break
    else: 
        icounter = icounter + 1
        print("Incorrect! Hint: it is a meme.")

icounter = 0

while icounter < 3:
    passwordguess3 = input("Guess the third password:")
    if passwordguess3 == (password3):
        point_counter + 1
        print("Correct!")
        break
    else:
        icounter = icounter + 1
        print("Incorrect! Hint: it is an emoticon.")
if point_counter > 2:
    print("Good job!")
if point_counter < 1:
    print("It's okay, we'll get there next time.")
print("Your points for the game:")
print(point_counter)
print("Day 2 will be unlocked soon!")
