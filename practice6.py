#Contact Book
from random import choice
from sys import path_hooks
from tkinter.font import names

Contact = {}

def ShowFuntion():
    print(Contact.items())
    print("Name \t Contact")
    for key in Contact:
        print("{} \t {}" .format(key, Contact.get(key)))
while True:
    choice =int( input("1. Add New Number\n"
                   "2. Search the Contact\n"
                   "3. Dispaly thr Contact\n"
                   "4. Edit the Contact\n"
                   "5. Delete the Contact\n"
                   "6. Exit\n"
                   "Please Write Number Between 1-6: "))

    if choice == 1:
        name = input ("Add Your Contact Name: ")
        phone = input ("Add Your Phone Number: ")
        Contact[name] = phone

    elif choice == 2:
        ContactName = input("Search Your Contact: ")
        if ContactName in Contact:
            print(ContactName, "contact name is ",Contact[ContactName])
        else:
            print("Not Found the Contact")

    elif choice == 3:
        if not Contact:
            print ("No Contact Found")
        else:
            ShowFuntion()


    elif choice == 4:
        EditContact = input("Edit Your Contact: ")
        if EditContact in Contact:
            phone = input("Change Your Phone Number: ")
            Contact[EditContact] = phone
            print("Contact Update Successfully ")
            ShowFuntion()
        else:
            print("Name is Not Found")


    elif choice == 5:
        DeleteConatact = input("Which Contact Do You Want To Delete?: ")
        if DeleteConatact in Contact:
            DeletedConfirm = input("Do You Want To Delete This Contact y/n")
            if DeletedConfirm == "y" or DeletedConfirm == "y":
                Contact.pop(DeletedConfirm)
            ShowFuntion()
        else:
            print("The Name is Not Found In The Contact")


    else:
        break

