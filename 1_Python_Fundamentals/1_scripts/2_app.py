# Import sys module for command-line argument parsing
import sys

def greet_user(user_name):
    """
    Greets the user with their name.

    param user_name: The name of the user.
    """
    print(f"Hello, {user_name}!")


if __name__ == "__main__":
    """
    Main entry point for the script.
    """
    if len(sys.argv) < 2:
        print("Usage: python 2_app.py <your_name>")
    else:
        greet_user(sys.argv[1])