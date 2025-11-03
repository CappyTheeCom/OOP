#Create a library system with class inheritence 


#Stores the title of the library item to be called upon later
class LibraryItem:

    def __init__(self, title):
        self.__title = title 

    @property
    def get_title(self):
        return self.__title


#Inherits the title from libraryitem as it shares the same attribute 
class Book(LibraryItem):

    #Adds further details of the book that can be called upon 
    def __init__(self,title, id, author):
        super().__init__(title)
        self.__id = id
        self.__author = author 
        self.__available = True
    
    @property
    def get_book_id(self):
        return self.__id
    
    @property
    def get_author(self):
        return self.__author
    
    @property
    def get_avialable(self):
        return self.__available
    
    #Allows to manuiplate the availability of the book while remaining a boolean value
    @get_avialable.setter
    def get_avialable(self,value):
        if not isinstance(value,bool):
            raise TypeError("Availability must be an error")
        #Allows for the availability variable to be changable in boolean values
        self.__available = value
        return self.__available
    

#Creates a seperate class of information towards the end user 
class Member:

    def __init__(self, member_id, name):
        self.__id = member_id
        self.__name = name
        self.__borrowed = []
    
    @property
    def get_member_id(self):
        return self.__id
    
    @property
    def get_member_name(self):
        return self.__name
    
    @property
    def get_borrowed_books(self):
        return self.__borrowed


#The main class that stores the book information 
class Library:

    def __init__(self):
        self.__books = [Book("The Hobbit",1,"J.K Tolkein"), Book("No Longer Human",2,"Osama Dazi"),Book("White Nights",3,"Fydor Dostovesky"),Book("The Great Gastby",4,"Scott Fiztgerald"),Book("I.T",5,"Stephen King")]
        self.__members = [Member(1,"Joe Rogan"),Member(2,"Jack Black"),Member(3,"Jessica Rabbit"),Member(4,"Samira Rodgers"),Member(5,"Ada Wong")]


    #Adds additional members into the program
    def add_new_member(self):
        add_member = input("Add member name: ")
        add_id = int(input("Add new  member ID: "))

        #Calls upon the member class and stores the information into the list
        #Checks if the user id is already in use
        for member_id in self.__members:
            if add_id == member_id.get_member_id:
                return print("ID is already in ")
        #Appends the new user information if Id not in use
        else:
            new_member = Member(add_id,add_member)
            self.__members.append(new_member)
            return self.__members
    
    #Adds new books into the program
    def add_new_booK(self):
        add_title = input("Enter title of the book: ")
        add_id = int(input("Enter ID of the book: "))
        add_author = input("Enter the author of the book: ")

        for book_id in self.__books:
            if add_id == book_id.get_book_id:
                return print("ID already in use")
        #Calls upon book class to store information into list
        else:
            new_book = Book(add_title,add_id,add_author)
            return self.__books.append(new_book)
    
    #Displays the library available books 
    def display_library(self):
            
        
            #uses a for loop to display the sequence of books that were added to the program
            print(f'{"Title:":<20}{"Author:":<25}{"ID:":>10}')
            for books in self.__books: 
                #Checks if the book has been borrowed by a user
                books.get_avialable = True
                for members in self.__members:
                    if books.get_book_id in members.get_borrowed_books:
                        #Changes the boolean value without changing the data type from the Book Class
                        books.get_avialable = False
                        break
                
                if books.get_avialable :
                    availability = "Available"
                else:
                    availability = "Unavailable"

                print(f"{books.get_title:<20}{books.get_author:<25}{books.get_book_id:>10}{availability:>15}")

    #Displays current members that were added to the system         
    def display_member(self):
            
            print(f'{"Name":<15}{"ID":<16}')
            for members in self.__members:
                 print(f"{members.get_member_name:<15}:{members.get_member_id:<16}")


    #Searches for members based on their ID alone         
    def search_member(self):
        #User inputs their id and the resulted name will come up, otherwise they are not found
        search_memberId = int(input("Enter member ID: "))

        print(f'{"Member:":<20}{"ID:":<25}')
        for member in self.__members:
            if search_memberId == member.get_member_id:
                print(f"{member.get_member_name:<20}{member.get_member_id:<25}")
                return
            
        #Returns not found 
        return print("Member not found")
    
    
    #Function to find a book based on its title 
    def search_book(self):
        #User input to find allocated name 
        search_book = input("Enter Book Name: ")

        #Loops through the list of books to find information about the book
        for book in self.__books:
            if search_book == book.get_title:
                print(f"Book: {book.get_title}, Authour: {book.get_author} ID:{book.get_book_id}")
                return
            
        #Returns not found if the user not in the list
        return print("Book not found")
    
    #Borrow book function 
    def borrow_book(self):
        apply_id = int(input("Enter your member ID: "))
        search_bookId = int(input("Enter the book Id you want to borrow: "))


            
        #Checks if the user id is present and checks if the book has already been borrowed 
        for borrower in self.__members:
            if search_bookId in borrower.get_borrowed_books:
                return print(f"Book is already borrowed")
            elif borrower.get_member_id == apply_id:
                break 
            else:
                return print("Member not found")
                
        #Checks if the book requested is available in the database, otherwise return as not found
        for books in self.__books:
            if search_bookId == books.get_book_id:
                print(f"You have now borrowed {books.get_title}")
                #Appends the members borrowed books into the borrow list
                for member in self.__members:
                    member.get_borrowed_books.append(books.get_book_id)
                    return member.get_borrowed_books
        else:
            print(f"Book has not been found.")
    

    #Return book function
    def return_book(self):
        apply_id = int(input("Enter your member ID: "))
        search_bookId = int(input("Enter the book ID you want to return: "))

        #Checks if the user is available, or if the book could not be found
        for member in self.__members:
            #Checks if the inputed id is within the current member database 
            if member.get_member_id == apply_id:
                #Checks if the borrowed book is currently borrowed
                if search_bookId in member.get_borrowed_books:
                    member.get_borrowed_books.remove(search_bookId)
                    return print("Book has been returned")
                elif not search_bookId in member.get_borrowed_books:
                    return print("Book could not be found")
            else:
                return print("Member not found")
    
    #Prints the allocated menu options 
    def __str__():
        print(" 1)Show book collection\n",
              "2)Add book\n",
              "3)Search book by name\n",
              "4)Show list of current members\n",
              "5)Add new member\n",
              "6)Search member by member ID\n",
              "7)Borrow Book\n",
              "8)Return Book\n",
              "9)Exit"
              )
            
        

#Allows to check for user input and the selection of what function to be used
def __main__():
    instance = Library()
    while True:
        Library.__str__()
        user_input = int(input("Please enter a number to access the library!: "))

        match user_input:
            case 1:
                instance.display_library()
            case 2:
                instance.add_new_booK()
            case 3:
                instance.search_book()
            case 4:
                instance.display_member()
            case 5:
                instance.add_new_member()
            case 6:
                instance.search_member()
            case 7:
                instance.borrow_book()
            case 8:
                instance.return_book()
            case 9:
                print("Good-bye!")
                break 
            case _:
                print("Input a valid option!")

if __name__ == "__main__":
    __main__()
            
                



                
            
            


