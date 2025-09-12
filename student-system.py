print("welcome to the greatest library  in the world")
books= [
    {"id": 1, "title": 1967, "book_name": "zlatan", "available": True},
    {"id": 2, "title": 2001, "book_name": "david goggins", "available": True},
    {"id": 3, "title": 2006, "book_name": "harry potter", "available": False},
    {"id": 4, "title": 2010, "book_name": "laws of power" , "available": True},]

while True:
    print("what would you like to do" )
    print("[0]-list all the books")
    print("[1]-borrow the book you want")
    print("[2]-add a book")
    print("[3]-remove a book")
    print("[q]-exit")

    choice = input ("enter your choice: ").strip()
    
    if choice == "0":
        print("list all the books:")
        for book in books:
            status ="available" if book["available"] else "not avalable"
            print(f'Id: {book["id"]} - {book["title"]} - {book["book_name"]}')
    
    elif choice == "1":
        print("borrow the book you want")
        for book in books:
            if book ["available"]:
                print(f'{book["id"]} - {book["book_name"]}')
    
        try:
            book_id = int(input("enter the id of the book you want"))  
        except ValueError:
            print("invalod number of the id")  
        found = False 
        for book in books:
            if book["id"] == book_id:
                found = True
                if book["available"]:
                    book["available"] = False 
                    print(f'You borrowed "{book["book_name"]}')
                else:
                    print("the book is already borrowed")
                    if not found:
                        print("book not found")
    elif choice == "2":
        print("add a book")
        new_id = int(input("enter the book id "))
        new_title =(input("title: "))
        new_name =(input("book_name: "))
        books.append({"id": new_id, "title": new_title,"book_name": new_name, "available": True})
        print("book added")

    elif choice == "3":
        print("remove a book")
        remove_id = (input("enter the book id you want to remove: "))
        for book in books:
            if book["id"] == remove_id:
                books.remove(book) 
                print("book removed")
                break
            else: 
                print("book not found") 
    elif choice == "q":
        print("goodbye")
        break

    else: 
        print("invalid choice")                                
