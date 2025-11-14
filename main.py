from library_books import library_books
from datetime import datetime, timedelta
import time

# -------- Level 1 --------
# TODO: Create a function to view all books that are currently available
# Output should include book ID, title, and author
def check_available(library_books):
    print("Available book: (title, author, book ID)")
    for book in library_books:
        if book["available"]:
            print(f'{book["title"]}, {book["author"]}, {book["id"]}')


# -------- Level 2 --------
# TODO: Create a function to search books by author OR genre
# Search should be case-insensitive
# Return a list of matching books
def search_books(library_books):
    search = input("Please enter the author or genre of the book(s) you are searching for: ")
    for book in library_books:
        if book["genre"].lower() == search.lower() or book["author"].lower() == search.lower():
            print(f'{book["title"]}')


# -------- Level 3 --------
# TODO: Create a function to checkout a book by ID
# If the book is available:
#   - Mark it unavailable
#   - Set the due_date to 2 weeks from today
#   - Increment the checkouts counter
# If it is not available:
#   - Print a message saying it's already checked out
def checkout(library_books):
    book_ID = input("Please enter the ID of the book you would like to checkout: ")
    for book in library_books:
        if book["id"] == book_ID:
            if book["available"]:
                book["available"] = False
                book["checkouts"] += 1 
                book["due_date"] = datetime.today() + timedelta(weeks=2)
            else:
                print("I'm sorry, that book is already checked out right now")



# -------- Level 4 --------
# TODO: Create a function to return a book by ID
# Set its availability to True and clear the due_date
def return_book(library_books):
    book_id = input("Please enter the ID of the book you want to return: ")
    for book in library_books:
        if book["id"] == book_id:
            book["available"] = True
            book["due_date"] = None

# TODO: Create a function to list all overdue books
# A book is overdue if its due_date is before today AND it is still checked out
def overdue_books(library_books):
    for book in library_books:
        if book["due_date"] != None:
            dueDate = datetime.strptime(book["due_date"], "%Y-%m-%d")
        else:
            dueDate = datetime.today()
        if book["available"] == False and dueDate < datetime.today():
            print(f'{book["title"]}')


# -------- Level 5 --------
# TODO: Convert your data into a Book class with methods like checkout() and return_book()
# TODO: Add a simple menu that allows the user to choose different options like view, search, checkout, return, etc.
class Book:

    def __init__(self, id, genre, title, author, available = True, due_date = None, checkouts = 0):
        self.id = id
        self.genre = genre
        self.title = title
        self.author = author
        self.available = available
        self.due_date = due_date
        self.checkouts = checkouts
    
    def checkout(self):
        if self.available:
            self.available = False
            self.checkouts += 1 
            self.due_date = datetime.today() + timedelta(weeks=2)
        else:
            print("I'm sorry, that book is already checked out right now")
   
    def checkin(self):
        self.available = True
        self.due_date = None


# -------- Optional Advanced Features --------
# You can implement these to move into Tier 4:
# - Add a new book (via input) to the catalog
# - Sort and display the top 3 most checked-out books
# - Partial title/author search
# - Save/load catalog to file (CSV or JSON)
# - Anything else you want to build on top of the system!

def top_3_books(library_books):
    max_1 = 0
    max_2 = 0
    max_3 = 0
    book_1 = ""
    book_2 = ""
    book_3 = ""
    for book in library_books:
        if book["checkouts"] > max_1:
            book_1 = book["title"]
            max_1 = book["checkouts"]
    for book in library_books:
        if book["checkouts"] > max_2 and book["checkouts"] < max_1:
            book_2 = book["title"]
            max_2 = book["checkouts"]
    for book in library_books:
        if book["checkouts"] > max_3 and book["checkouts"] < max_2:
            book_3 = book["title"]
            max_3 = book["checkouts"]
    print(f'Number 1 with {max_1} checkouts: {book_1}')
    print(f'Number 2 with {max_2} checkouts: {book_2}')
    print(f'Number 3 with {max_3} checkouts: {book_3}')
            
if __name__ == "__main__":

    while True:
        print("\n--- Library Menu ---")
        print("1. View available books")
        print("2. Search books by author or genre")
        print("3. Checkout a book")
        print("4. Return a book")
        print("5. View overdue books")
        print("6. View Most Checked Out Books")
        print("7. Exit")

        choice = input("Choose an option (1-7): ")

        if choice == "1":
            check_available(library_books)
            time.sleep(4)
        elif choice == "2":
            search_books(library_books)
            time.sleep(4)
        elif choice == "3":
            checkout(library_books)
            time.sleep(4)
        elif choice == "4":
            return_book(library_books)
            time.sleep(4)
        elif choice == "5":
            overdue_books(library_books)
            time.sleep(4)
        elif choice == "6":
            top_3_books(library_books)
            time.sleep(4)
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please enter a number between 1 and 6.")
