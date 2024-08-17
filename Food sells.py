def food_store():
  """
  A simple food selling store program using dictionaries and lists.
  """
  # Define a dictionary to store food items with their prices
  menu = {
    "pizza": 20.99,
    "burger": 12.50,
    "fries": 11.25,
    "soda": 5.50,
    "chicken wings": 11.75,
  }

  # Initialize an empty list to store the user's order
  order = []

  # Main loop to keep the store running
  while True:
    # Display menu and available items
    print("\nWelcome to the Food Store!")
    print("Menu:")
    for item, price in menu.items():
      print(f"{item}: ${price:.2f}")

    # Display order (if any)
    if order:
      print("\nYour Order:")
      total = 0
      for item, quantity in order:
        print(f"{quantity} x {item} - ${menu[item] * quantity:.2f}")
        total += menu[item] * quantity
      print(f"Total: ${total:.2f}")

    # Display options
    print("\nWhat would you like to do?")
    print("1. Add item to order")
    print("2. Remove item from order")
    print("3. Checkout")
    print("4. Exit")

    # Get user input for their choice
    choice = input("Enter your choice (1-4): ")

    # Handle user choices using conditional statements
    if choice == "1":
      # Add item to order
      item = input("Enter the item you want: ").lower()
      if item in menu:
        quantity = int(input(f"How many {item}s do you want? "))
        order.append((item, quantity))
        print(f"{quantity} {item}(s) added to your order!")
      else:
        print(f"Sorry, we don't have {item} on the menu.")
    elif choice == "2":
      # Remove item from order
      if not order:
        print("Your order is empty!")
      else:
        item = input("Enter the item you want to remove: ").lower()
        found = False
        for i, (order_item, _) in enumerate(order):
          if order_item == item:
            del order[i]
            found = True
            print(f"{item} removed from your order.")
            break
        if not found:
          print(f"{item} not found in your order.")
    elif choice == "3":
      # Checkout
      if not order:
        print("Your order is empty!")
      else:
        # Calculate total and print receipt
        total = 0
        for item, quantity in order:
          total += menu[item] * quantity
        print("\n--- Receipt ---")
        for item, quantity in order:
          print(f"{quantity} x {item} - ${menu[item] * quantity:.2f}")
        print(f"Total: ${total:.2f}")
        print("Thank you for your order!")
        order.clear()  # Clear the order after checkout
    elif choice == "4":
      # Exit the store
      print("Thank you for visiting the Food Store!")
      break
    else:
      # Invalid choice
      print("Invalid choice. Please try again.")

# Run the food store program
food_store()
