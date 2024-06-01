

class Student:
    def __init__(self, name, id_number, course):
        self.name = name
        self.id_number = id_number
        self.course = course 
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.available_copies > 0:
            self.borrowed_books.append(book)
            book.available_copies -= 1
            print(f"Book '{book.title} 'has been borrowed by {self.name}.")
        else:
            print(f"Sorry,'{book.title}'is not available right now.")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.available_copies += 1
            print(f"Book'{book.title}'has been returned by {self.name}.")
        else:
            print(f"You did not borrow '{book.title}'from the library")

    def check_available_books(self,book):
        print(f"Available copies of '{book.title}': {book.available_copies}")


class Librarian:
    def __init__(self, name, id_number):
        self.name = name 
        self.id_number = id_number

    def insert_book(self,book, quantity):
        book.available_copies += quantity
        print(f"Added {quantity} copies of '{book.title}' to the library.")

    def remove_book(self, book):
        del book
        print(f"Book '{book.title}' has been remove from the library. ")

    def check_available_books(self, book):
        print(f"Available copies of '{book.title}': {book.available_copies}")

class Book:
    def __init__(self, title, author, publisher, total_copies):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.total_copies = total_copies

    #INSERT THE WHILE LOOP
def runThis():
    #account = {}
    book = True

    print("========================================")
    print("Welcome to the L.M.S")

    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    publication = input("Enter the publication information: ")
    copies = int(input("Enter the total number of copies: "))

    my_library = Book(title,author,publication,copies)
    librarian = Librarian("Librarian Name: ", "Librarian ID: ")

    while book == True:
            print("========================================")

            print("Options:")
            print("========================================")
            print("1. Add a book : ")
            print("========================================")
            print("2. Borrow a book : ")
            print("========================================")
            print("3. Check Available Books : ")
            print("========================================")
            print("4. Return Books : ")
            print("========================================")
            print("5. Check how many Books Available : ")
            print("========================================")
            print("6. Exit : ")
            print("========================================")
                

            choice = int(input("Enter your choice: "))

            if choice == 1:
                #add
                book_title = input("Enter the title of the book: ")
                book_author = input("Enter the author of the book: ")
                book_publication = input("Enter The Publication Information: ")
                no_copies = int(input("Enter the total copies: "))
                my_library = Book(book_title,book_author,book_publication,no_copies)
                librarian.book_list.append(my_library)
                print("\n Book Added Successfully! ")
                

            if choice == 2:
                #borrow
                student_name = input("Enter student name: ")
                student_ID = input("Enter a Student Id: ")
                student_course =input("Enter student course: ")
                librarian.borrow(student_name,student_ID,student_course)


            if choice == 3:
                #check
                librarian.check_available_books()
                

            if choice == 4:
                #return
                student_ID = int(input("Enter Student ID: "))
                librarian.return_book(student_ID)
                

            if choice == 5:
                #hm copies available
                available_copies = librarian.check_available_books()
                print(f"Available Copies : {available_copies} ")

            elif choice == 6:
                print("Closing the Library Management System")
                print("Thank You, Goodbye!")
                break
            else:
                print("Invalid Choice. Please Try Again.")
                

runThis()                       

