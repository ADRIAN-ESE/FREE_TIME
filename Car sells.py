# Define a Car class to store car details
class Car:
    def __init__(self, make, model, year, price):
        self.make = make
        self.model = model
        self.year = year
        self.price = price

    def display_details(self):
        print(f"{self.year} {self.make} {self.model} - ${self.price:,.2f}")


# Initialize an empty car inventory list
inventory = []


def main_menu():
    print("\nWelcome to the Car Dealership!")
    print("1. View Inventory")
    print("2. Add Car")
    print("3. Sell Car")
    print("4. Exit")
    choice = input("Enter your choice: ")
    return choice


def view_inventory():
    if not inventory:
        print("There are no cars in the inventory.")
    else:
        print("\nCurrent Inventory:")
        for car in inventory:
            car.display_details()


def add_car():
    make = input("Enter car make: ")
    model = input("Enter car model: ")
    try:
        year = int(input("Enter car year: "))
    except ValueError:
        print("Invalid year. Please enter a number.")
        return
    try:
        price = float(input("Enter car price: "))
    except ValueError:
        print("Invalid price. Please enter a number.")
        return
    new_car = Car(make, model, year, price)
    inventory.append(new_car)
    print("Car added successfully!")


def sell_car():
    if not inventory:
        print("There are no cars to sell.")
        return
    view_inventory()
    try:
        choice = int(input("Enter the index of the car to sell (or 0 to cancel): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    if choice == 0:
        return
    if 0 <= choice < len(inventory):
        car_to_sell = inventory[choice - 1]
        print(f"\nSelling {car_to_sell.year} {car_to_sell.make} {car_to_sell.model}")
        inventory.remove(car_to_sell)
        print("Car sold successfully!")
    else:
        print("Invalid choice. Please select a car from the list.")


# Main program loop
while True:
    choice = main_menu()
    if choice == '1':
        view_inventory()
    elif choice == '2':
        add_car()
    elif choice == '3':
        sell_car()
    elif choice == '4':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")
