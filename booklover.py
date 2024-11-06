
class BookLover:
    """
    A class to represent a book lover.

    Attributes:
    ----------
    name : str
        Name of the book lover.
    email : str
        Email of the book lover.
    fav_genre : str
        Favorite genre of the book lover.
    num_books : int
        Number of books read by the book lover.
    book_list : list
        A list of books with their ratings.
    """

    def __init__(self, name, email, fav_genre, num_books=0, book_list=None):
        """
        Initialize the BookLover with name, email, favorite genre, and optionally,
        the number of books and a list of books they have read.
        """
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        self.book_list = [] if book_list is None else book_list

    def add_book(self, book_name, rating):
        """
        Add a new book to the book list with its rating. Only add the book
        if it's not already in the list.
        """

        if book_name not in [book['name'] for book in self.book_list]:
            self.book_list.append({'name': book_name, 'rating': rating})
            self.num_books += 1

    def has_read(self, book_name):
        """
        Check if the book lover has already read a particular book.
        """
        return any(book['name'] == book_name for book in self.book_list)

    def num_books_read(self):
        """
        Return the total number of books read.
        """
        return len(self.book_list)

    def fav_books(self):
        """
        Return a list of books that have a rating greater than 3 (favorite books).
        """
        return [book for book in self.book_list if book['rating'] > 3]
