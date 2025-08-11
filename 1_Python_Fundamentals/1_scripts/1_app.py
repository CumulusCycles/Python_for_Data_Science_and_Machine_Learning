# This App prompts the user for their name then greets them.

# Declare a variable named user_name to store the user's name
# Obtain the user's name through input
user_name = input("Please enter your name: ")

# Greet the user
if user_name == "":
    print("Sorry, you didn't enter your name.")
else:
    print(f"Hello, {user_name}!")
