import os

FOLDER = 'contacts/'
TXT_FILE = '.txt'

class Contact:
    def __init__(self, name, address, telephone, email, category):
        self.name = name
        self.address = address
        self.telephone = telephone
        self.email = email
        self.category = category


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
            add_contact()
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
            print("\r\n----------------------------------------------------------\r\n")      

def display_menu():
    print("\r\n----------------------------------------------------------\r\n")
    print("HELLO, WELCOME TO THIS AMAZING APP ʕ•́ᴥ•̀ʔっ \r\n")
    print("Please select from this menu what you would like to do: \r\n")
    print("1) Add a new contact")
    print("2) Edit contact")
    print("3) Display my contacts")
    print("4) Search contact")
    print("5) Delete contact")
    print("\r\n----------------------------------------------------------\r\n")


def add_contact():
    print("\r\n----------------------------------------------------------\r\n")
    print("Enter your new contact information ٩(˘◡˘)۶")
    contact_name = input("Contact name: \r\n")
    print("----------------------------------------------------------")

    # To check if a contact already exits
    exist = os.path.isfile(FOLDER + contact_name + TXT_FILE)

    if not exist:
        with open(FOLDER + contact_name + TXT_FILE, "w") as archive:
            address = input("Address: \r\n")
            print("----------------------------------------------------------")
            telephone = input("Telephone: \r\n")
            print("----------------------------------------------------------")
            email = input("Email: \r\n")
            print("----------------------------------------------------------")
            category = input("Category: \r\n")
            print("----------------------------------------------------------")

            contact = Contact(contact_name, address, telephone, email, category)

            archive.write("Name: " + contact.name + "\n")
            archive.write("Address: " + contact.address + "\n")
            archive.write("Telephone: " + contact.telephone + "\n")
            archive.write("Email: " + contact.email + "\n")
            archive.write("Category: " + contact.category + "\n")

            print("\r\n**********************************************************\r\n")
            print("WELL DONE!!! CONTACT SUCCESSFULLY CREATED ٩(˘◡˘)۶ \r\n")
            print("**********************************************************\r\n")
    else:
        print("\r\nSorry, this contact already exist, try again (ㆆ_ㆆ)\r\n")
    
    MyApp()

def create_directory():
    if not os.path.exists(FOLDER):
        # It creates a new folder called "contacts"
        os.makedirs(FOLDER)
    else:
        print('This folder already exits')


MyApp()