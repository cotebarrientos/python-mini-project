import os

FOLDER = 'contacts/'

def MyApp():
    # To check if the folder was created
    create_directory()


def create_directory():
    if not os.path.exists(FOLDER):
        # It creates a new folder called "contacts"
        os.makedirs(FOLDER)
    else:
        print('This folder already exits')


MyApp()