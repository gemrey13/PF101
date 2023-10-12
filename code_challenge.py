from library import Book, Librarian, Student  # Assuming your library classes are in a module named "library"

book_list = []
librarian = Librarian('Goku', 123)

run = True
login = False
user_type = None

while run:
    

    if login == True:
        if user_type == "student":
            print("""
                [1] Borrow Book
                [2] Return Book
                [3] Check Available Books
                [4] Logout
            """)
            choice = input('> ')

            if choice == '1':
                title = input("Enter the title of the book to borrow: ")
                no_copies = int(input("Enter the number of copies to borrow: "))
                student.borrow_book(title, no_copies)

            elif choice == '2':
                title = input("Enter the title of the book to return: ")
                no_copies = int(input("Enter the number of copies to return: "))
                student.return_book(title, no_copies)

            elif choice == '3':
                available_books = librarian.check_books_available(book_list)
                print("Available books:")
                for book in available_books:
                    print(f"{book.title} - Copies available: {book.no_copies}")

            elif choice == '4':
                print("Logging out...")
                login = False

            else:
                print("Invalid choice. Please try again.")

        elif user_type == "librarian":
            print("""
                [1] Add Book
                [2] Remove Book
                [3] Check Available Books
                [4] Logout
            """)
            choice = input("> ")

            if choice == '1':
                title = input("Enter the title of the book: ")
                author = input("Enter the author of the book: ")
                publisher = input("Enter the publisher of the book: ")
                no_of_copies = int(input("Enter the number of copies: "))

                librarian.insert_book(title, author, publisher, no_of_copies)
                print(f"{title} added to the library.")

            elif choice == '2':
                title = input("Enter the title of the book to remove: ")
                librarian.remove_book(title)

            elif choice == '3':
                available_books = librarian.check_books_available(book_list)
                print("Available books:")
                for book in available_books:
                    print(f"{book.title} - Copies available: {book.no_copies}")

            elif choice == '4':
                print("Logging out...")
                login = False

            else:
                print("Invalid choice. Please try again.")


    if login == False:
        print("""
            [1] Librarian Login
            [2] Student Login
            [3] Create Student Account
            [4] Exit
        """)
        choice = input("> ")

        if choice == '1':
            print("Please log in as a librarian.")
            librarian_name = str(input("Enter librarian name: "))
            librarian_id = int(input("Enter librarian ID: "))

            if librarian_name == librarian.librarian_name and librarian_id == librarian.id_no:
                print("Librarian login successful.")
                login = True
                continue
            else:
                print("Invalid librarian credentials. Please try again.")

        elif choice == '2':
            print("Please log in as a student.")
            student_name = input("Enter your name: ")
            student_idno = input("Enter your ID number: ")
            student_course = input("Enter your course: ")

            student = Student(student_name, student_idno, student_course)
            login = True
            print("Student login successful.")

        elif choice == '3':
            print("Creating a new student account.")
            student_name = input("Enter your name: ")
            student_idno = input("Enter your ID number: ")
            student_course = input("Enter your course: ")

            student = Student(student_name, student_idno, student_course)
            login = True
            print("Student account created and logged in.")

        elif choice == '4':
            print("Exiting program...")
            run = False

        else:
            print("Invalid choice. Please try again.")