import os

FOLDER = 'contacts/'

def MyApp():
    # To check if the folder was created
    create_directory()

    display_menu()

    # Ask a user about an option from the menu
    ask_user = True
    while ask_user:
        option = input("Select an option from this menu \r\n")
        option = int(option)

        # To execute the menu options
        if option == 1:
            print("Add a new contact")
            ask_user = False
        elif option == 2:
            print("Edit contact")
            ask_user = False
        elif option == 3:
            print("Display my contacts")
            ask_user = False  
        elif option == 4:
            print("Search contact")
            ask_user = False  
        elif option == 5:
            print("Delete contact")
            ask_user = False
        else:
            print("Sorry, invalid option, try again (ㆆ_ㆆ)")
            print("\r\n----------------------------------------------------------")      

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