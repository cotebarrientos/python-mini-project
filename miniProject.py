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
    # To display the menu
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
            edit_contact()
            ask_user = False
        elif option == 3:
            display_contacts()
            ask_user = False  
        elif option == 4:
            search_contact()
            ask_user = False  
        elif option == 5:
            delete_contact()
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


def display_contacts():
    archives = os.listdir(FOLDER)

    txt_archives = [i for i in archives if i.endswith(TXT_FILE)] 

    print("\r\n----------------------------------------------------------\r\n")
    print("ALL YOUR CONTACTS ٩(˘◡˘)۶")
    print("\r\n----------------------------------------------------------\r\n")

    for archive in txt_archives:
        with open(FOLDER + archive) as my_contacts:
            for line in my_contacts:
                print(line.rstrip())
            print("\r\n----------------------------------------------------------\r\n")                   
    
    MyApp()


def search_contact():
    print("\r\n----------------------------------------------------------\r\n")
    print("SEARCH A CONTACT ٩(˘◡˘)۶")
    print("\r\n----------------------------------------------------------\r\n")
    select_contact = input("Select a contact to search for: \r\n")

    try:
        with open(FOLDER + select_contact + TXT_FILE) as contact:
            print("\r\n----------------------------------------------------------\r\n")
            print("YOUR CONTACT INFORMATION (≖_≖ )")
            print("\r\n----------------------------------------------------------\r\n")
            for line in contact:
                print(line.rstrip())
            print("\r\n----------------------------------------------------------\r\n")
    except IOError: 
        print("\r\nSorry, this contact doesn't exist, try again (ㆆ_ㆆ)\r\n")

    MyApp()


def add_contact():
    print("\r\n----------------------------------------------------------\r\n")
    print("ENTER YOUR NEW CONTACT INFORMATION ٩(˘◡˘)۶")
    print("\r\n----------------------------------------------------------\r\n")
    contact_name = input("Contact name: \r\n")
    print("----------------------------------------------------------")

    # To check if a contact already exits
    exist = contact_exist(contact_name)

    if not exist:
        with open(FOLDER + contact_name + TXT_FILE, "w") as archive:
            address = input("Address: \r\n")
            print("----------------------------------------------------------")
            telephone = input("Telephone: \r\n")
            print("----------------------------------------------------------")
            email = input("Email: \r\n")
            print("----------------------------------------------------------")
            category = input("Category: \r\n")

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


def edit_contact():
    print("\r\n----------------------------------------------------------\r\n")
    print("ENTER THE CONTACT YOU WANT TO EDIT ٩(˘◡˘)۶")
    print("\r\n----------------------------------------------------------\r\n")
    previous_name = input("Contact name: \r\n")
    print("----------------------------------------------------------") 

    exist =  contact_exist(previous_name)  

    if exist:
        with open(FOLDER + previous_name + TXT_FILE, "w") as archive:
            new_name = input("Enter a new contact name: \r\n")
            print("----------------------------------------------------------")
            new_address = input("Enter a new address: \r\n")
            print("----------------------------------------------------------")
            new_telephone = input("enter a new telephone: \r\n")
            print("----------------------------------------------------------")
            new_email = input("Enter a new Email: \r\n")
            print("----------------------------------------------------------")
            new_category = input("Enter a new category: \r\n")

            contact = Contact(new_name, new_address, new_telephone, new_email, new_category)

            archive.write("Name: " + contact.name + "\n")
            archive.write("Address: " + contact.address + "\n")
            archive.write("Telephone: " + contact.telephone + "\n")
            archive.write("Email: " + contact.email + "\n")
            archive.write("Category: " + contact.category + "\n")

        # Rename the current archive
        os.rename(FOLDER + previous_name + TXT_FILE, FOLDER + new_name + TXT_FILE)

        print("\r\n**********************************************************\r\n")
        print("WELL DONE!!! CONTACT SUCCESSFULLY EDITED ٩(˘◡˘)۶ \r\n")
        print("**********************************************************\r\n")            

    else:
        print("\r\nSorry, this contact doesn't exist (ㆆ_ㆆ)\r\n")
    
    MyApp()


def delete_contact():
    print("\r\n----------------------------------------------------------\r\n")
    print("ENTER THE CONTACT YOU WANT TO DELETE ٩(˘◡˘)۶")
    print("\r\n----------------------------------------------------------\r\n")
    contact_name = input("Contact name: \r\n")
    try:
        os.remove(FOLDER + contact_name + TXT_FILE)
        print("\r\n**********************************************************\r\n")
        print("WELL DONE!!! CONTACT SUCCESSFULLY EDITED ٩(˘◡˘)۶ \r\n")
        print("**********************************************************\r\n")
    except IOError:
        print("\r\nSorry, this contact doesn't exist, try again (ㆆ_ㆆ)\r\n")

    MyApp()


def contact_exist(name):
    return os.path.isfile(FOLDER + name + TXT_FILE)


def create_directory():
    if not os.path.exists(FOLDER):
        # It creates a new folder called "contacts"
        os.makedirs(FOLDER)
    else:
        print('This folder already exits')


MyApp()