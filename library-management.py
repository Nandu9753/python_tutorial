
import sys
class Library:
    books=[]
    authers=[]
    def addBook(self):
        name = input("Enter a Book Name: ")
        auther = input("Enter a name: ")
        book= Book(name,auther)
        self.books.append(book)
        return self.books.index(book)
    def addAuther(self):
        name = input("Enter a Name: ")
        mobile = input("Enter a mobile: ")
        auther= Auther(name,mobile)
        self.authers.append(auther)
        return self.authers.index(auther)
    def getAuthor(self):
        if(len(library.authers) != 0):
            for author in library.authers:
                print(author.name)
        return False 
    def getBook(self):
        if(len(library.books) != 0):
            for book in library.books:
                print(book.name)
        return False            
class Book:
    def __init__(self, name, auther):
      self.name = name
      self.auther =auther

    
    
class Auther:
    def __init__(self, name, email):
        self.name = name
        self.email =email
library=Library()
def menu():
    a = '''
    \nWelcome to library managment tool\n
    --------------------------------------------
    chose a munu option\n
    ---------------------
    1. add author
    2. add book
    3. show author
    4. show book
    5. remove author
    6. remove books
    7. export
    8. exit
    ---------------------------------
    '''
    print(a)
while(True):
    menu()
    n = input("Enter a Option: ")
    if(n=="1"):
        library.addAuther()
    elif(n=="2"):
        library.addBook()
    elif(n=="3"):
        author = library.getAuthor()
        if author:
            print(author)
    elif(n=="4"):
        book = library.getBook()
        if(book):
            print(book)
    else:
        sys.exit()

