#dict
phonebook = {
    "AMIT":"9876543210",
    "RIYA":"9123456780"
    }

#feature window
def features():
    try: 
        print("1. ADD CONTACT")
        print("2. SEARCH CONTACT")
        print("3. DELETE CONTACT")
        choose = int(input("Please choose what you want to do."))
    except ValueError:
        print("Please enter a valid integer")
    
    if choose == 1:
        add_contact()
    elif choose == 2:
        search_contact()
    elif choose == 3:
        delete_contact()
    else:
        print("Please enter 1-3")
        features()

#main features
def add_contact():
    name = input("Please enter a name: ").upper()
    phone = input("Please enter the Number: ")
    if name in phonebook:
        print("This name is already in the phonebook, try something else")
    else:
        phonebook[name] = phone
        print("Contact added succesfully!")
    print(phonebook)
    features()

def search_contact():
    search = input("Please enter the name to search: ").upper()

    found = False

    for name, number in phonebook.items():
        if search in name:
            print(f"{name} : {number}")
            found = True

    if found == False:
        print("No matching contact found")
    features()
    
def delete_contact():
    print(phonebook)
    remove = input("Which contact do you want to delete").upper()
    if remove in phonebook:
        del phonebook[remove]
        print("Contact deleted\n")
    else:
        print("Contact not found\n")
    print(phonebook)
    features()

features()
