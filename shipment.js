const readline = require('readline');

class Shipment {
    constructor(id, origin, destination, weight, status, paymentMethod) {
        this.id = id;
        this.origin = origin;
        this.destination = destination;
        this.weight = weight;
        this.status = status;
        this.paymentMethod = paymentMethod;
    }
}

let shipments = [];
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function addShipment() {
    rl.question("Enter shipment ID: ", (id) => {
        rl.question("Enter origin: ", (origin) => {
            rl.question("Enter destination: ", (destination) => {
                rl.question("Enter weight (kg): ", (weight) => {
                    rl.question("Enter initial status (Pending, In Transit, Delivered): ", (status) => {
                        rl.question("Enter payment method (Cash, Card, Bank Transfer): ", (paymentMethod) => {
                            shipments.push(new Shipment(parseInt(id), origin, destination, parseFloat(weight), status, paymentMethod));
                            mainMenu();
                        });
                    });
                });
            });
        });
    });
}

function displayShipments() {
    console.log("-".repeat(70));
    console.log("ID\tOrigin\t\tDestination\tWeight (kg)\tStatus\t\tPayment Method");
    console.log("-".repeat(70));
    shipments.forEach((shipment) => {
        console.log(`${shipment.id}\t${shipment.origin.padEnd(20)}\t${shipment.destination.padEnd(20)}\t${shipment.weight.toFixed(2)}\t${shipment.status}\t${shipment.paymentMethod}`);
    });
    console.log("-".repeat(70));
    mainMenu();
}

function updateStatus() {
    rl.question("Enter shipment ID to update: ", (id) => {
        const found = shipments.find((shipment) => shipment.id === parseInt(id));
        if (found) {
            rl.question("Enter new status: ", (newStatus) => {
                found.status = newStatus;
                mainMenu();
            });
        } else {
            console.log("Shipment not found.");
            mainMenu();
        }
    });
}

function searchShipments() {
    rl.question("Enter origin or destination to search: ", (searchTerm) => {
        shipments.forEach((shipment) => {
            if (shipment.origin.toLowerCase().includes(searchTerm.toLowerCase()) || shipment.destination.toLowerCase().includes(searchTerm.toLowerCase())) {
                console.log(`ID: ${shipment.id}`);
                console.log(`  Origin: ${shipment.origin}`);
                console.log(`  Destination: ${shipment.destination}`);
                console.log(`  Weight: ${shipment.weight.toFixed(2)} kg`);
                console.log(`  Status: ${shipment.status}`);
                console.log(`  Payment Method: ${shipment.paymentMethod}`);
                console.log("-".repeat(20));
            }
        });
        mainMenu();
    });
}

function mainMenu() {
    console.log("\nShipping Management System");
    console.log("1. Add Shipment");
    console.log("2. Display Shipments");
    console.log("3. Update Shipment Status");
    console.log("4. Search Shipments");
    console.log("5. Exit");

    rl.question("Enter your choice: ", (choice) => {
        switch (choice) {
            case "1":
                addShipment();
                break;
            case "2":
                displayShipments();
                break;
            case "3":
                updateStatus();
                break;
            case "4":
                searchShipments();
                break;
            case "5":
                console.log("Exiting program.");
                rl.close();
                break;
            default:
                console.log("Invalid choice.");
                mainMenu();
        }
    });
}

mainMenu();