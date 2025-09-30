#Names: Akintunde Udo, Mishka Mansukhani
#Date: September 23, 2025
#Description: The user is given options of what to do with a list of contacts, such as finding new ones
# or looking up specific information and when they're done they can save their changes

import check_input
import contacts

def read_file():
    #Takes a txt file and uploads the contents into a list and returns said list
    contact_list = []
    file = open("addresses.txt", "r")
    for line in file:
        con = line.strip().split(',')
        contact_list.append(contacts.Contact(con[0], con[1], con[2], con[3], con[4], con[5]))
        contact_list.sort()
    return contact_list

def write_file(contact_list):
    #Takes in a new contact in the form of a list then opens the txt file for writing in order to add new contact
    file = open("addresses.txt", "w")
    for c in contact_list:
        file.write(repr(c) + "\n")
    file.close()

def get_menu_choice():
    #Displays a menu where the user enters a number between 1-5 then returns their choice
    menu = "Rolodex Menu\n 1. Display Contacts\n 2. Add Contact\n 3. Search Contact\n 4. Modify Contact\n 5. Save & Quit"
    print(menu)
    user_choice = check_input.get_int_range("Please choose from the following options: ", 1, 5)
    return user_choice

def modify_contact(cont):
    #Displays a menu where the user can choose how they want to modify an already existing contact
    option = 0
    while option != 7:
        print("Modify Menu:")
        print("1. First name")
        print("2. Last name")
        print("3. Phone")
        print("4. Address")
        print("5. City")
        print("6. Zip")
        print("7. Save")

        choice = check_input.get_int_range("Make a selection:", 1, 7)

        if choice == 1:
            cont.first_name = input("Enter first name: ")
        elif choice == 2:
            cont.last_name = input("Enter last name: ")
        elif choice == 3:
            cont.phone_number = input("Enter phone #: ")
        elif choice == 4:
            cont.address = input("Enter address: ")
        elif choice == 5:
            cont.city = input("Enter city: ")
        elif choice == 6:
            cont.zip = input("Enter zip: ")
        elif choice == 7:
            option = 7

def main():
    #Loads contacts from file, displays a menu for viewing, adding, searching, and modifying contacts, and saves all changes on exit.
    con_list = read_file()
    choice = get_menu_choice()
    while choice != 5:
        if choice == 1:
            #Displays all the contacts
            print(f"Number of contacts: {len(con_list)}")
            for i, con in enumerate(con_list):
                print(str(i + 1) + " " + str(con) + "\n")

        elif choice == 2:
            #Allows the user to add a new contact
            print("Enter new contact:")
            f_name = input("First name: ")
            l_name = input("Last name: ")
            phone = input("Phone number: ")
            addr = input("Address: ")
            city = input("City: ")
            z_code = input("Zip: ")  # keep as string
            new_contact = contacts.Contact(f_name, l_name, phone, addr, city, z_code)
            con_list.append(new_contact)
            con_list.sort()

        elif choice == 3:
            #Searches for contacts by last name or zip
            print("Search:\n1. Search by last name\n2. Search by zip")
            num_choice = check_input.get_int_range(">", 1, 2)

            if num_choice == 1:
                last_name = input("Enter last name: ")
                for ln in con_list:
                    if ln.last_name == last_name:
                        print(str(ln) + "\n")

            if num_choice == 2:
                zip_code = input("Enter zipcode: ")
                for code in con_list:
                    if code.zip == zip_code:
                        print(str(code) + "\n")

        elif choice == 4:
            #Allows the user to modify an existing contact
            fn = input("Enter first name:")
            ln = input("Enter last name:")
            print()
            for c in con_list:
                if fn == c.first_name and ln == c.last_name:
                    print(c)
                    modify_contact(c)
            con_list.sort()

        choice = get_menu_choice()

    #Saves all the contacts and exits the program
    write_file(con_list)
    print("Saving File...\nEnding Program")

main()
