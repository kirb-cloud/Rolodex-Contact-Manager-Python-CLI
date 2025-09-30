# Rolodex-Contact-Manager-Python-CLI
A lightweight and interactive **Command-Line Contact Manager** built in Python. This application allows users to **load, view, search, add, edit, and save contacts** stored in a simple text file format — perfect for learning file handling, classes, and input validation.

## Features

| Feature | Description |
|---------|-------------|
| Persistent Storage | Contacts are saved in `addresses.txt` and reloaded on startup. |
| Display Contacts | View all contacts with numbering. |
| Search Functionality | Search by **Last Name** or **ZIP Code**. |
| Edit Existing Contacts | Modify first name, last name, phone, address, city, or ZIP. |
| Add New Contacts | Create and sort new contact entries. |
| Input Validation | Robust integer and yes/no validation via `check_input.py`. |

## Project Structure

rolodex-contact-manager
│── main.py: Core program logic & menu system
│── contacts.py: Contact class (data model + sorting + formatting)
│── check_input.py: Input validation utilities
│── addresses.txt: Stored contacts
│── README.md: Project documentation


## Example Interface, Input, Output

Rolodex Menu
 1. Display Contacts
 2. Add Contact
 3. Search Contact
 4. Modify Contact
 5. Save & Quit
Please choose from the following options: 1

Number of contacts: 2  
1 John Doe  
 555-1234  
 123 Elm St  
 Pleasantville 90210  




