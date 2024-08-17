def phonebook():
    """
  A simple phone book application using a dictionary.
  """
    contacts = {}  # Empty dictionary to store contacts

    while True:
        print("\nPhone Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter contact name: ")
            number = input("Enter phone number: ")
            contacts[name] = number  # Add contact to dictionary
            print(f"{name} has been added to the phone book.")

        elif choice == '2':
            if not contacts:
                print("Your phone book is empty.")
            else:
                print("\nContacts:")
                for name, number in contacts.items():
                    print(f"{name}: {number}")

        elif choice == '3':
            name = input("Enter the name to search: ")
            if name in contacts:
                print(f"{name}'s phone number is: {contacts[name]}")
            else:
                print(f"{name} not found in the phone book.")

        elif choice == '4':
            name = input("Enter the name to delete: ")
            if name in contacts:
                del contacts[name]
                print(f"{name} has been deleted from the phone book.")
            else:
                print(f"{name} not found in the phone book.")

        elif choice == '5':
            print("Exiting phone book...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    phonebook()
