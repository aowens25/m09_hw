import unittest
from booklover import BookLover

class TestBookLover(unittest.TestCase):

    def test_add_book(self):
        bl = BookLover("John Doe", "john@example.com", "Fiction")
        bl.add_book("Harry Potter", 5)
        self.assertTrue(bl.has_read("Harry Potter"))  
    
    def test_has_read(self):
        bl = BookLover("John Doe", "john@example.com", "Fiction")
        self.assertFalse(bl.has_read("The Hobbit"))  
        bl.add_book("The Hobbit", 4)
        self.assertTrue(bl.has_read("The Hobbit"))  

    def test_num_books_read(self):
        bl = BookLover("John Doe", "john@example.com", "Fiction")
        self.assertEqual(bl.num_books_read(), 0)  
        bl.add_book("Harry Potter", 5)
        self.assertEqual(bl.num_books_read(), 1)  
    
    def test_fav_books(self):
        bl = BookLover("John Doe", "john@example.com", "Fiction")
        bl.add_book("Harry Potter", 5)
        bl.add_book("Twilight", 2)
        fav_books = bl.fav_books()
        self.assertEqual(len(fav_books), 1)  

if __name__ == '__main__':
    unittest.main()