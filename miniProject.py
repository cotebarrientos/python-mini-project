import os

FOLDER = 'contacts/'

def MyApp():
    # To check if the folder was created
    create_directory()

    display_menu()


def display_menu():
    print("\r\n---------------------------------------------------------- \r\n")
    print("HELLO, WELCOME TO THIS AMAZING APP ʕ•́ᴥ•̀ʔっ \r\n")
    print("Please select from this menu what you would like to do: \r\n")
    print("1) Add a new contact")
    print("2) Edit contact")
    print("3) Display my contacts")
    print("4) Search contact")
    print("5) Delete contact")
    print("\r\n----------------------------------------------------------")


def create_directory():
    if not os.path.exists(FOLDER):
        # It creates a new folder called "contacts"
        os.makedirs(FOLDER)
    else:
        print('This folder already exits')


MyApp()