contact_book = {}

def display_menu():
    print("Contact Book Menu:")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. List All Contacts")
    print("6. Exit")
def add_contact(contact_book):
    name = input()
    phone = input()
    email = input()
    address = input()
    if name in contact_book:
        print("Contact already exists!")
    else:
        contact_book[name] = {
            "phone": phone,
            "email": email,
            "address": address
        }
        print("Contact added successfully!")
def view_contact(contact_book):
    name = input()
    if name in contact_book:
        print(f"Name: {name}")
        print(f"Phone: {contact_book[name]['phone']}")
        print(f"Email: {contact_book[name]['email']}")
        print(f"Address: {contact_book[name]['address']}")
    else:
        print("Contact not found!")
def edit_contact(contact_book):
    name = input()
    if name in contact_book:
        phone = input()
        email = input()
        address = input()
        contact = contact_book[name]
        if phone == '':
            phone = contact["phone"]
        if email == "":
            email = contact["email"]
        if contact == "":
            address = contact["address"]
        contact_book[name] = {"phone":phone, "email":email, "address": address}
        print("Contact updated successfully!")
    else:
        print("Contact not found!")
def delete_contact(contact_book):
    name = input()
    if name in contact_book:
        del contact_book[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")
def list_all_contacts(contact_book):
    if not contact_book:
        print("No contacts available.")
    else:
        for name in contact_book:
            print("Name:",name)
            print("Phone:",contact_book[name]["phone"])
            print("Email:",contact_book[name]["email"])
            print("Address:",contact_book[name]["address"])
            print("")

while True:
    inp = int(input())
    display_menu()
    if not inp or inp > 6:
        print("Invalid choice. Please try again.")
    elif inp == 1:
        add_contact(contact_book)
    elif inp == 2:
        view_contact(contact_book)
    elif inp == 3:
        edit_contact(contact_book)
    elif inp == 4:
        delete_contact(contact_book)
    elif inp == 5:
        list_all_contacts(contact_book)
    elif inp == 6:
        break