def contact_book():
    contacts = {}
    
    while True:
        print("\nContact Book:")
        print("1. Add contact")
        print("2. Remove contact")
        print("3. Search contact")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            contacts[name] = phone
        elif choice == '2':
            name = input("Enter name to remove: ")
            if name in contacts:
                del contacts[name]
            else:
                print("Contact not found")
        elif choice == '3':
            name = input("Enter name to search: ")
            if name in contacts:
                print(f"{name}: {contacts[name]}")
            else:
                print("Contact not found")
        elif choice == '4':
            break
        else:
            print("Invalid option")

contact_book()
