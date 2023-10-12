class Student:
    def __init__(self, name, idno, course):
        self.name = name
        self.idno = idno
        self.course = course

    def borrow_book(self, book):
        if book.no_of_copies > 0:
            book.no_of_copies -= 1
            print(f"{self.name} has borrowed {book.title}")
        else:
            print(f"{book.title} is not available for borrowing.")

    def return_book(self, book):
        book.no_of_copies += 1
        print(f"{self.name} has returned {book.title}")

class Librarian:
    def __init__(self, name, idno):
        self.name = name
        self.idno = idno

    def insert_book(self, title, author, publisher, no_of_copies):
        return Book(title, author, publisher, no_of_copies)

    def remove_book(self, book):
        del book

    def check_books_available(self, books):
        available_books = []
        for book in books:
            if book.no_of_copies > 0:
                available_books.append(book)
        return available_books

class Book:
    def __init__(self, title, author, publisher, no_of_copies):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.no_of_copies = no_of_copies

library = []
librarian = Librarian("Goku",123)
while True:
    print("1 - Add Book")
    print("2 - Remove Book")
    print("3 - Check Available Books")
    print("4 - Borrow Book")
    print("5 - Return Book")
    print("6 - Exit")
    
    choice = eval(input("Enter your choice: "))
    
    if choice == 1:
        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        publisher = input("Enter the publisher of the book: ")
        no_of_copies = eval(input("Enter the number of copies: "))
        
        book = Book(title, author, publisher, no_of_copies)
        
        library.append(book)
        
    elif choice == 2:
        title = input("Enter the title of the book to remove: ")
        
        for book in library:
            if book.title == title:
                Librarian.remove_book(book)
                break
                
    elif choice == 3:
        print("Available books:")
        
        for book in librarian.check_books_available(library):
            print(book.title)
            
    elif choice == 4:
        title = input("Enter the title of the book to borrow: ")
        
        for book in library:
            if book.title == title and book.no_of_copies > 0:
                student_name = input("Enter your name: ")
                student_idno = input("Enter your ID number: ")
                student_course = input("Enter your course: ")
                
                student = Student(student_name, student_idno, student_course)
                
                student.borrow_book(book)
                
                break
                
            elif book.title == title and book.no_of_copies == 0:
                print(f"{book.title} is not available for borrowing.")
                
                break
                
    elif choice == 5:
        title = input("Enter the title of the book to return: ")
        
        for book in library:
            if book.title == title:
                student_name = input("Enter your name: ")
                
                for attribute in vars(student):
                    if getattr(student, attribute) != None:
                        print(f"{attribute}: {getattr(student, attribute)}")
                
                student.return_book(book)
                
                break
                
            elif library.index(book) == len(library) - 1 and book.title != title:
                print(f"{title} is not found in the library.")
                
    elif choice == 6:
        break
