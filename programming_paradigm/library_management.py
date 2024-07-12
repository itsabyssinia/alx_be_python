class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track checkout status

    def checkout(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        else:
            return False

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        else:
            return False
        

class Library:
    def __init__(self):
        self._books = []  # Private list to store Book instances

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if not book.checkout():
                    return f"Book '{title}' is already checked out."
                else:
                    return f"Checked out '{title}' successfully."
        return f"Book '{title}' not found in the library."

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if not book.return_book():
                    return f"Book '{title}' is not checked out."
                else:
                    return f"Returned '{title}' successfully."
        return f"Book '{title}' not found in the library."

    def list_available_books(self):
        available_books = [book.title + " by " + book.author for book in self._books if not book._is_checked_out]
        if available_books:
            for book in available_books:
                print(book)
        else:
            print("No books available in the library.")

