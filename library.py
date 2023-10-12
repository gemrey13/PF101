book_list = []

class Student:
    def __init__(self, student_name, id_no, course) -> None:
        self.student_name = student_name
        self.id_no = id_no
        self.course = course
        self.borrowed_books = []

    def borrow_book(self, title, no_copies):
        for book in range(0, len(book_list)):
            if book_list[book].title == title and book_list[book].no_copies >= no_copies:
                book_list[book].borrow_book(no_copies)
                self.borrowed_books.append((book_list[book], no_copies))
                book_list[book].borrow_book(no_copies)
                print(f"{self.student_name} has borrowed {no_copies} copies of '{title}'")
                break
        else:
            print(f"Sorry, not enough copies of '{title}' available.")

    def return_book(self, title, no_copies):
        for borrowed_book, num_borrowed in self.borrowed_books:
            if borrowed_book.title == title:
                if num_borrowed >= no_copies:
                    borrowed_book.return_book(no_copies)
                    self.borrowed_books.remove((borrowed_book, num_borrowed))
                    print(f"{self.student_name} has returned {no_copies} copies of '{title}'")
                else:
                    print(f"\nError: {self.student_name} did not borrow {no_copies} copies of '{title}'")
                break
        else:
            print(f"\nError: {self.student_name} did not borrow '{title}' or has already returned it.")

        
class Librarian:
    def __init__(self, librarian_name, id_no) -> None:
        self.librarian_name = librarian_name
        self.id_no = id_no

    def insert_book(self, title, author, publisher, no_copies):
        new_book = Book(title, author, publisher, no_copies)
        book_list.append(new_book)

    def remove_book(self, title):
        for book in range(0, len(book_list)):
            if book_list[book].title == title:
                print('A book was removed')
                book_list.pop(book)
                break

    def check_book(self):
        for book in range(0, len(book_list)):
            print(f"""
                [Book No. {book + 1}]
                Title         : {book_list[book].title}
                Author        : {book_list[book].author}
                Publisher     : {book_list[book].publisher}
                No. of copies : {book_list[book].no_copies}
            """)


class Book:
    def __init__(self, title, author, publisher, no_copies=0) -> None:
        self.title = title
        self.author = author
        self.publisher = publisher
        self.no_copies = no_copies

    def borrow_book(self, no_borrow):
        if self.no_copies >= no_borrow:
            self.no_copies -= no_borrow

    def return_book(self, no_return):
        self.no_copies += no_return


# gem = Librarian('Gem', 565)
# gem.insert_book('haha', 'me', 'ggg', 5)
# gem.insert_book('nge', 'asd', 'zxca', 6)

# gem.check_book()
# gem.remove_book('nge')
# for book in range(0, len(book_list)):
#     if book_list[book].title == 'haha':
#         book_list[book].borrow_book(3)
#         break
# gem.check_book()
# gem = Librarian('Gem', 565)
# gem.insert_book('haha', 'me', 'ggg', 5)
# gem.insert_book('nge', 'asd', 'zxca', 6)

# student = Student('Alice', 123, 'Computer Science')

# gem.check_book()
# student.borrow_book('haha', 4)
# student.check_available_book()

# student.return_book('haha', 1)
# student.check_available_book()
# gem.check_book()
