import sqlite3 
import sys
import hashlib
import os
icounter = 0
point_counter = 0
def exit_game():
    sys.exit()

def new_point():
    global point_counter
    point_counter += 5

def del_point():
    global point_counter
    point_counter -= 1
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

try:
    # Connect to SQLite database in a file
    conn = sqlite3.connect('name_password.db')

    # Create a cursor
    c = conn.cursor()

    # Create table
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (username hash, password hash, salt blob)''')
    salt = os.urandom(16)
    

    hashed_username = hashlib.pbkdf2_hmac('sha256', name.encode(), salt, 100000)
    hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)

    # Insert a row of data
    c.execute("INSERT INTO users VALUES (?, ?, ?)", (hashed_username, hashed_password, salt))

    # Save (commit) the changes
    conn.commit()

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    conn.close()
class Question:
    def ask(self, password, hint):
        while icounter < 3:
           passwordguess = input("Guess the first password: ")
           if passwordguess == (password):
              new_point()
              print("Correct!")
              break
           else: 
              del_point()
              print(hint)
              icounter = icounter + 1
password1 = ("minecraft")
password2 = ("quertyuiop1234")
password3 = (":(")
question = Question()
print("Oh no! Hackers are trying to get into your system and have locked your computer! Guess the passwords for all three systems to win!")
print("Entering system 1...")
print("In!")
question.ask(password1, "It's a popular video game.")
icounter = 0

question.ask(password2, "It's a meme about passwords.")
icounter = 0

question.ask(password3, "HAL.DLL not found!")
icounter = 0
if point_counter > 2:
    print("Good job!")
if point_counter < 1:
    print("It's okay, we'll get there next time.")
print("Your points for the game:")
print(point_counter)
print("Day 2 has been unlocked!")
print("Welcome to hackGAME 2.0!")
print("What's new: you can play the new classic levels, the new gamemode, or you can make levels!")
print("Type 1 to play classic levels!\n Type 2 to play the new gamemode!,\n or Type 3 to make levels!")
