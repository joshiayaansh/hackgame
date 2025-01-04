import sqlite3
import sys
import hashlib
import os
import subprocess
# Globals for game
icounter = 0
point_counter = 0

# Functions for the game
def exit_game():
    sys.exit()

def new_point():
    global point_counter
    point_counter += 5

def del_point():
    global point_counter
    point_counter -= 1

def hash_with_salt(value, salt):
    """Hashes a value with a given salt using SHA-256."""
    return hashlib.pbkdf2_hmac('sha256', value.encode(), salt, 100000)

def initialize_db():
    """Creates the database and users table if they don't exist."""
    conn = sqlite3.connect('name_password.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password_hash BLOB,
            salt BLOB
        )
    ''')
    conn.commit()
    conn.close()

def check_if_users_exist():
    """Checks if there are any users in the database."""
    conn = sqlite3.connect('name_password.db')
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM users")
    count = c.fetchone()[0]
    conn.close()
    return count > 0

def register_user(username, password):
    """Registers a new user with a salted and hashed password."""
    salt = os.urandom(16)
    password_hash = hash_with_salt(password, salt)
    
    conn = sqlite3.connect('name_password.db')
    c = conn.cursor()
    try:
        c.execute("INSERT INTO users VALUES (?, ?, ?)", (username, password_hash, salt))
        conn.commit()
        print("User registered successfully.")
    except sqlite3.IntegrityError:
        print("Username already exists!")
    finally:
        conn.close()

def verify_user(username, password):
    """Verifies a username and password against the database."""
    conn = sqlite3.connect('name_password.db')
    c = conn.cursor()
    c.execute("SELECT password_hash, salt FROM users WHERE username = ?", (username,))
    result = c.fetchone()
    conn.close()

    if not result:
        return False
    
    stored_hash, salt = result
    input_hash = hash_with_salt(password, salt)
    return stored_hash == input_hash

# Password guessing game
class Question:
    def ask(self, password, hint, num):
        global icounter
        while icounter < 3:
            passwordguess = input(f"Guess the {num} password: ")
            if passwordguess == password:
                new_point()
                print("Correct!")
                break
            else: 
                del_point()
                print(hint)
                icounter += 1

# Main program
initialize_db()

if check_if_users_exist():
    print("Welcome back!")
    login_username = input("Enter your username: ")
    login_password = input("Enter your password: ")
    
    if verify_user(login_username, login_password):
        print("Login successful!")
    else:
        print("Invalid username or password.")
        exit_game()
else:
    print("No users found. Let's create your account!")
    name = input("Enter your username: ")
    password = input("Enter a password to keep your account safe: ")
    register_user(name, password)

# The guessing game begins!
print("\nWelcome to the hacking terminal portal!")
print("Oh no! Hackers are trying to get into your system and have locked your computer! Guess the passwords for all three systems to win!")
question = Question()

password1 = "minecraft"
password2 = "quertyuiop1234"
password3 = ":("

print("\nEntering system 1...")
num = "first"
question.ask(password1, "It's a popular video game.", num)
icounter = 0


num = "second"
question.ask(password2, "It's a meme about passwords.", num)
icounter = 0


num = "third"
question.ask(password3, "HAL.DLL not found!", num)

# Show results
if point_counter > 2:
    print("\nGood job!")
else:
    print("\nIt's okay, we'll get there next time.")

print(f"Your points for the game: {point_counter}")
print("Welcome to hack_game 2.0!! In 2.0 you can play new classic levels \n, or play the new gamemode!")
choice = input("Press 1 to play new classics\n, or press 2 to play the new gamemode!")
if choice == "1":
    print("Entering system 2\n")
    password4 = "iloveyou.doc.vbs"
    password5 = "wannacry.exe"
    password6 = "whoami"
    num = "fourth"
    question.ask(password4, "An old worm from the 1990s.", num)
    icounter = 0
    num = "fifth"
    question.ask(password5, "A ransomware from 2020.", num)
    icounter = 0
    num = "sixth"
    question.ask(password6, "A command in Windows for checking the current user.", num)
elif choice == "2":
    subprocess.run(["UPDATE.exe"])
print("Thanks for playing!")
