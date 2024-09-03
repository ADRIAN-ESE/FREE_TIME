const readline = require('readline');

class PhoneBook {
    constructor() {
        this.contacts = {}; // Empty object to store contacts
        this.rl = readline.createInterface({
            input: process.stdin,
            output: process.stdout
        });
    }

    addContact() {
        this.rl.question("Enter contact name: ", (name) => {
            this.rl.question("Enter phone number: ", (number) => {
                this.contacts[name] = number; // Add contact to object
                console.log(`${name} has been added to the phone book.`);
                this.run();
            });
        });
    }

    viewContacts() {
        if (Object.keys(this.contacts).length === 0) {
            console.log("Your phone book is empty.");
        } else {
            console.log("\nContacts:");
            for (const name in this.contacts) {
                console.log(`${name}: ${this.contacts[name]}`);
            }
        }
        this.run();
    }

    searchContact() {
        this.rl.question("Enter the name to search: ", (name) => {
            if (name in this.contacts) {
                console.log(`${name}'s phone number is: ${this.contacts[name]}`);
            } else {
                console.log(`${name} not found in the phone book.`);
            }
            this.run();
        });
    }

    deleteContact() {
        this.rl.question("Enter the name to delete: ", (name) => {
            if (name in this.contacts) {
                delete this.contacts[name];
                console.log(`${name} has been deleted from the phone book.`);
            } else {
                console.log(`${name} not found in the phone book.`);
            }
            this.run();
        });
    }

    displayMenu() {
        console.log("\nPhone Book Menu:");
        console.log("1. Add Contact");
        console.log("2. View Contacts");
        console.log("3. Search Contact");
        console.log("4. Delete Contact");
        console.log("5. Exit");
    }

    run() {
        this.displayMenu();
        this.rl.question("Enter your choice (1-5): ", (choice) => {
            switch (choice) {
                case '1':
                    this.addContact();
                    break;
                case '2':
                    this.viewContacts();
                    break;
                case '3':
                    this.searchContact();
                    break;
                case '4':
                    this.deleteContact();
                    break;
                case '5':
                    console.log("Exiting phone book...");
                    this.rl.close();
                    break;
                default:
                    console.log("Invalid choice. Please try again.");
                    this.run();
            }
        });
    }
}

const phoneBook = new PhoneBook();
phoneBook.run();