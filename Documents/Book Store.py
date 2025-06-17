import uuid
import json

class Book:
    def __init__(self, title, author, genre, price, stock):
        self.book_id = str(uuid.uuid4())
        self.title = title
        self.author = author
        self.genre = genre
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Genre: {self.genre}, Price: ${self.price}, Stock: {self.stock}, ID: {self.book_id}"

    def to_dict(self):
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "genre": self.genre,
            "price": self.price,
            "stock": self.stock
        }

class OnlineBookstore:
    def __init__(self, shelf_file="shelf.json"):
        self.books = {}
        self.cart = []
        self.shelf_file = shelf_file
        self.load_shelf()

    def load_shelf(self):
        try:
            with open(self.shelf_file, "r") as f:
                data = json.load(f)
                for book_data in data:
                    book = Book(
                        book_data["title"],
                        book_data["author"],
                        book_data["genre"],
                        book_data["price"],
                        book_data["stock"]
                    )
                    book.book_id = book_data["book_id"]
                    self.books[book.book_id] = book
        except FileNotFoundError:
            print("Shelf file not found. Creating a new one.")
            self.save_shelf() #create empty file
        except json.JSONDecodeError:
            print("Shelf file is corrupted. Creating a new one.")
            self.save_shelf() #create empty file

    def save_shelf(self):
        data = [book.to_dict() for book in self.books.values()]
        with open(self.shelf_file, "w") as f:
            json.dump(data, f, indent=4)

    def add_book(self, title, author, genre, price, stock):
        book = Book(title, author, genre, price, stock)
        self.books[book.book_id] = book
        self.save_shelf()
        print(f"Book '{book.title}' added successfully with ID: {book.book_id}")

    def search_book(self, query):
        results = []
        for book in self.books.values():
            if query.lower() in book.title.lower() or query.lower() in book.author.lower() or query.lower() in book.genre.lower():
                results.append(book)
        return results

    def add_to_cart(self, book_id, quantity):
        book = self.books.get(book_id)
        if book:
            if book.stock >= quantity:
                self.cart.append({"book": book, "quantity": quantity})
                print(f"{quantity} copies of '{book.title}' added to cart.")
            else:
                print(f"Insufficient stock for '{book.title}'. Available stock: {book.stock}")
        else:
            print("Book not found.")

    def view_cart(self):
        if not self.cart:
            print("Your cart is empty.")
        else:
            total_price = 0
            print("Your Cart:")
            for item in self.cart:
                book = item["book"]
                quantity = item["quantity"]
                subtotal = book.price * quantity
                print(f"{quantity} x '{book.title}' - ${book.price} each - Subtotal: ${subtotal}")
                total_price += subtotal
            print(f"Total: ${total_price}")

    def checkout(self, payment_method):
        if not self.cart:
            print("Your cart is empty. Nothing to checkout.")
            return

        total_price = 0
        for item in self.cart:
            book = item["book"]
            quantity = item["quantity"]
            subtotal = book.price * quantity
            total_price += subtotal
            book.stock -= quantity #Reduce stock
        print(f"Checkout successful! Total: ${total_price}, Payment Method: {payment_method}")
        self.cart = [] #Empty cart after checkout
        self.save_shelf() #update stock in shelf

def main():
    bookstore = OnlineBookstore()

    while True:
        print("\nOnline Bookstore")
        print("1. Add Book")
        print("2. Search Book")
        print("3. Add to Cart")
        print("4. View Cart")
        print("5. Checkout")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            genre = input("Enter book genre: ")
            price = float(input("Enter book price: "))
            stock = int(input("Enter book stock: "))
            bookstore.add_book(title, author, genre, price, stock)

        elif choice == "2":
            query = input("Enter search query (title, author, or genre): ")
            results = bookstore.search_book(query)
            if results:
                print("Search Results:")
                for book in results:
                    print(book)
            else:
                print("No books found.")

        elif choice == "3":
            book_id = input("Enter book ID: ")
            quantity = int(input("Enter quantity: "))
            bookstore.add_to_cart(book_id, quantity)

        elif choice == "4":
            bookstore.view_cart()

        elif choice == "5":
            payment_method = input("Enter payment method (Credit Card/PayPal/etc.): ")
            bookstore.checkout(payment_method)

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()