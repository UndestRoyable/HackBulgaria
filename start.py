import sql_manager
import getpass


def main_menu():
    print("Welcome to our bank service. You are not logged in.")
    print("Please register or login")

    while True:
        command = input("$$$>")

        if command == 'register':
            username = input("Enter your username: ")
            password = getpass.getpass("Enter your password: ")
            email = input("Enter your email: ")

            sql_manager.register(username, password, email)

        elif command == 'login':
            username = input("Enter your username: ")
            password = getpass.getpass("Enter your password: ")

            logged_user = sql_manager.login(username, password)

            if logged_user:
                logged_menu(logged_user)
            else:
                print("Login failed")

        elif command == 'send-reset-password':
            username = input("Enter your username: ")
            sql_manager.send_reset_pass_email(username)

        elif command == 'reset-password':
            username = input("Enter your username: ")
            hash = input("Enter the hash code from your email: ")
            sql_manager.reset_password(username, hash)

        elif command == 'help':
            print("login - for logging in!")
            print("register - for creating new account!")
            print("exit - for closing program!")

        elif command == 'exit':
            break

        else:
            print("Not a valid command")


def logged_menu(logged_user):
    print("Welcome you are logged in as: " + logged_user.get_username())
    while True:
        command = input("Logged>>")

        if command == 'info':
            print("You are: " + logged_user.get_username())
            print("Your id is: " + str(logged_user.get_id()))
            print("Your balance is:" + str(logged_user.get_balance()) + '$')

        elif command == 'changepass':
            new_pass = getpass.getpass("Enter your new password: ")
            sql_manager.change_pass(new_pass, logged_user)

        elif command == 'change-message':
            new_message = input("Enter your new message: ")
            sql_manager.change_message(new_message, logged_user)

        elif command == 'show-message':
            print(logged_user.get_message())

        elif command == 'deposit':
            amount = input("Enter the amount of money you want to deposit: ")
            tan = input("Enter TAN code: ")
            sql_manager.deposit(amount, tan, logged_user)

        elif command == 'withdraw':
            amount = input("Enter the amount of money you want to withdraw: ")
            tan = input("Enter TAN code: ")
            sql_manager.withdraw(amount, tan, logged_user)

        elif command == 'display-balance':
            print(sql_manager.display_balance(logged_user))

        elif command == 'get-tan':
            sql_manager.get_tan(logged_user)

        elif command == 'help':
            print("info - for showing account info")
            print("changepass - for changing passowrd")
            print("change-message - for changing users message")
            print("show-message - for showing users message")

        elif command == 'logout':
            break


def main():
    sql_manager.create_clients_table()
    main_menu()

if __name__ == '__main__':
    main()
