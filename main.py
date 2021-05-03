import pickle
import os

class Contact():
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return "Name: {0}\nPhone: {1}\nEmail: {2}".format(self.name, self.phone, self.email)


def get_contact_info():
    contact_name = input("Enter full name: ")
    contact_phone = input("Enter phone number: ")
    contact_email = input("Enter email address: ")
    contact = Contact(contact_name, contact_phone, contact_email)
    return contact

def add_contact():
    contact_file = open("Contacts.txt", "rb")
    check_file = os.path.getsize("Contacts.txt")==0
    if not check_file:
        contacts_list = pickle.load(contact_file)
    else:
        contacts_list = []
    try:
        contact = get_contact_info()
        contact_file = open("Contacts.txt", "wb")
        contacts_list.append(contact)
        pickle.dump(contacts_list, contact_file)
        print("Contact saved!")
        contact_file.close()
        start_program()
    except Exception as e:
        print(e)

def start_program():
    user_input = input("Create a new contact:[1] Find a contact:[2] Display all contacts:[3] :")
    if user_input == "1":
        add_contact()
    elif user_input == "2":
        find_contact()
    elif user_input == "3":
        display_all_contacts()
    else:
        print("Invalid input: LOL")
        start_program()

def display_all_contacts():
    contact_file = open("Contacts.txt", "rb")
    pickle_load = pickle.load(contact_file)
    for contacts in pickle_load:
        print(contacts)
    else:
        start_program()



def find_contact():
    contact_file = open("Contacts.txt", "rb")
    check_file = os.path.getsize("Contacts.txt") == 0
    if not check_file:
        search_contact = input("Enter name of contact: ")
        contacts_list = pickle.load(contact_file)
        for contact in contacts_list:
            contact_name = contact.name
            search_contact = search_contact.lower()
            contact_name = contact_name.lower()
            if contact_name == search_contact:
                print(contact)
                start_program()


start_program()





