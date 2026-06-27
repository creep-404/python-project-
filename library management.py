# library management system program 

from datetime import datetime , timedelta

# nested directory to store all the records 
# ISBN number as the key 

books ={
    "LIB204-1":{"title":"the simple path to wealth","author":"jl collins","available":True,"borrower":None,"borrow_id":None,"issue_date":"none"},
    "LIB204-2":{"title":"project hail marry","author":"andy weir","available":True,"borrower":None,"borrow_id":None,"issue_date":"none"},
    "LIB204-3":{"title":"Metamorphosis","author":"franz kafka","available":False,"borrower":"shahid ahmad khan","borrow_id":"STU001","issue_date":"21/05/2026"},
    "LIB204-4":{"title":"the shining","author":"stephan king","available":True,"borrower":None,"borrow_id":None,"issue_date":"none"},
    "LIB204-5":{"title":"the stranger","author":"albert camus","available":True,"borrower":"none","borrow_id":"none","issue_date":"none"},
    "LIB204-6":{"title":"atomic habits","author":"james clear","available":False,"borrow_id":"STU002","issue_date":"29/05/2026"},
    "LIB204-7":{"title":"the communist manifesto","author":"karl marx","available":True,"borrow_id":"none","issue_date":"none"},


    }

# calculating the due date by adding 7 days to issue date 

def check_due_date(issue_date):
    d = datetime.strptime(issue_date, "%d-%m-%y")
    due = d + timedelta(days=7)
    return due.strftime("%d-%m-%y")


def add_book():
    print("===add book===")
    isbn = input("enter ISBN:").strip()


    if isbn in books:
        print("book with ISBN already exist:")
        return
    
    title = input("book title:").strip()
    author = input("authors name:").strip()

    if not title or not author:
        print("title and author cant be empty:")
        return
    

    # setting default values when new book is added 

    books[isbn] = {
        "title": title,
        "author": author,
        "available": True,
        "borrower": None,
        "borrow_id": None,
        "issue_date": None
    }

    print("done the book is added:")




def issue_book():
    print("===issue book===:")
    isbn = input("enter ISBN:").strip()


    if isbn not in books:
        print("book is not found:")
        return
    
    b = books [isbn]


    # checking if book is available for issue 
    if b["available"] == False:
        print(f"sorry this book is already issued to {b['borrower']}")
        return
    
    name = input("borrower name:").strip()
    sid = input("student id:").strip()


    if not name or not sid:
        print("name and id cant be empty:")
        return
    

    # storing current date as a issue date
    today=datetime.now().strftime("%d-%m-%y")
    due = check_due_date(today)


    books[isbn]["available"] = False
    books[isbn]["borrower"] = name
    books[isbn]["borrower_id"] = sid
    books[isbn]["issue_date"] = today


    print("book issued succesfully:")
    print(f"title     : {b['title']}")
    print(f"issued to : {name}({sid})")
    print(f"due date  : {due}")




def return_book():
    print("===return book===")
    isbn = input("enter ISBN:").strip()


    if isbn not in books:
        print("book is not found:")
        return

    b = books[isbn]


    # checking if book is already available before processing return 
    if b["available"]== True:
        print("this book is not issued , available:")
        return
    
    print(f"returning book: {b['title']}")
    print(f"borrower:{b['borrower']} ({b['borrow_id']})")


    # clearing borrowe information and marking book as available 

    books[isbn]["available"] = True
    books[isbn]["borrower"] = None
    books[isbn]["borrow_id"] = None
    books[isbn]["issue_date"] = None

    print("book is returned succesfully:")



def search_book():
    print("===search book===:")
    kw = input("enter title or author to search").strip().lower()

    found = 0
    for isbn, b in books.items():
        # display records where the entered keyword matches with the book title or authors name 
        if kw in b["title"].lower() or kw in b["author"].lower():
            status = "available" if b["available"] else f"issued to {b['borrower']}"
            print(f"ISBN   :{isbn}")
            print(f"title   :{b['title']}")
            print(f"author  :{b['author']}")
            print(f"status  :{status}")
            found+=1

    if found == 0:
        print("no books found:")
    else:
        print(f"{found} book(s) found")   


def view_catalog():
    if not books:
        print("no books in the library:")
        return
    
    print()
    print("-"*75)
    print(f"{'ISBN':<10} {'Title':<22} {'Author':<18} {'Status'}")
    print("-"*75)


    for isbn, b in books.items():
        # display book status if the book is available or else show "issued"
        status = "available" if b["available"] else "issued"
        print(f"{isbn:<10} {b['title']:<22} {b['author']:<18} {status}")   


    print("-"*75)
    print(f"total books:{len(books)}")


def show_menu():
    print("=====LIBRARY MANAGEMENT SYSTEM=====")
    print("1: add book")    
    print("2: issue book")
    print("3: return book")
    print("4: search book")
    print("5: view catelog")
    print("6: exit")



#main program starts here
while True:
    show_menu()
    ch = input("choice: ")
 
    if ch == '1':
        add_book()
    elif ch == '2':
        issue_book()
    elif ch == '3':
        return_book()
    elif ch == '4':
        search_book()
    elif ch == '5':
        view_catalog()
    elif ch == '6':
        print("bye!")
        break
    else:
        print("wrong choice, try again")


             