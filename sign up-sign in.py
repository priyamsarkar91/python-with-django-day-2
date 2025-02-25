users = {}

def sign_up():
    """Function to handle user signup."""
    while True:
        email = input("Enter your email to sign up: ").strip()
        if email in users:
            print("This email is already registered. Try signing in.")
            continue
        
        password = input("Create a password: ")
        confirm_password = input("Confirm your password: ")
        
        if password == confirm_password:
            users[email] = password
            print("Signup successful! You can now sign in.")
            break
        else:
            print("Passwords do not match. Try again.")

def sign_in():
    """Function to handle user sign-in."""
    while True:
        email = input("Enter your email to sign in: ").strip()
        password = input("Enter your password: ")

        if email in users and users[email] == password:
            print("Sign in successful! Welcome.")
            break
        else:
            print("Invalid email or password. Try again.")

# Main loop
while True:
    print("\n1. Sign Up\n2. Sign In\n3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        sign_up()
    elif choice == "2":
        sign_in()
    elif choice == "3":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")