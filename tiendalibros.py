import sys

#List of inventory
inv = []

#list of genres
genre = ["Fiction", "Non-fiction", "Science", "Biography", "Children"]

#Adding function
def add_book(inv, nam, aut, amo, gen):

    inv.append({"name": nam, "author": aut, "amount": amo, "genre": gen, "borrowed" : 0})
    print(f"\nThe book {nam} was added succesfully!")
    return inv

#searching function
def search(inv, nam):
    for book in inv:
        if book["name"].lower().strip() == nam.lower().strip():
            return book
    print(f"Book {nam} was not found")
    return None

#Function for borrowing books
def book_loan(inv, nam):
    for book in inv:
        if book["name"].lower().strip() == nam.lower().strip():
            if book["amount"] >= 1:
                book["amount"] -= 1
                book["borrowed"] +=1
                print(f"\nBook {nam} borrowed succesfully!")
                return
            else: print("\nBook is out of existances")
    print(f"\nBook {nam} was not found")

#Function for returning books
def book_return(inv, nam):
    for book in inv:
        if book["name"].lower().strip() == nam.lower().strip():
            if book["borrowed"] >= 1:
                book["amount"] += 1
                book ["borrowed"] -= 1
                print(f"\nBook {nam} returned succesfully!")
                return
            else:print(f"\nWe haven't borrowed {nam}")
            return
    print(f"\nBook {nam} was not found")


#function for deleting a book
def delete_book(inv, nam):
    for i, book in enumerate(inv):
        if book["name"].lower().strip() == nam.lower().strip():
            if book["borrowed"] == 0:
                del inv[i]
                print(f"\nBook {nam} deleted succesfully")
                return
            else:
                print(f"\nWe have at least 1 copy of {nam} borrowed, please try again when they return it")
                return
    print(f"\nBook {nam} was nos found")


#Function to list books
def list_books(inv, genre):
    if not inv:
            print("There are no books in the inventory")
            return
    for g in genre:
        for book in inv:
            if book["genre"] == g:
                print(f"""
Books of {book["genre"]}
Name: {book["name"]}
Author: {book["author"]}
Amount: {book["amount"]}\n""")
                     
#Exit function
def exit():
    print("\nSee you soon...\n")
    sys.exit()


#Functions that aren't in the requirements but maybe we need them

#Function to change amount of books
def change_amount(inv, nam, newamo):
    for book in inv:
        if book["name"].lower().strip() == nam.lower().strip():
            book["amount"] = newamo
            print(f"Amount of book {nam} updated succesfully!")
            return
    print(f"Book {nam} was not found")


#Function to clear all inventory
def clear_inventory(inv):
    for i, book in enumerate(inv):
        if book["borrowed"] == 0:
            print(f"Deleting book {book["name"]} from inventory")
            del inv[i]
        elif book["borrowed"] >= 1:
            print(f"Book {book["name"]} has at least 1 copy borrowed, can't delete")
        else:
            print(f"Book {book["name"]} can't be deleted" )



#creating menu
def menu():
    print("""\n
--------------------------------------
          Select an option:
    1. Add book
    2. Search book
    3. List books
    4. Borrow books
    5. Return books
    6. Update amount
    7. Delete book
    8. Clear inventory
    9. Exit
--------------------------------------\n""")
    while True:
        try:
            opc = int(input("Select your option: "))
            if 0<opc<=9:
                return opc
            else:
                print("\nSelect a valid option")
        except ValueError:
            print("Select a valid option")


#Start the app
print("""
------------------------------------
             Welcome
------------------------------------""")

while True:
    opc = menu()
    match opc:
        #Adding a book
        case 1:
            nam = str(input("Enter your books name: "))
            aut = str(input("Who is the author of this book: "))
            while True:
                try:
                    amo = int(input("How many copies do you have: "))
                    if amo >0:
                        break
                    else: 
                        print("Insert a valid amount")
                except ValueError:
                    print("Insert a valid amount")
            print("""
What is the genre of your book?
1. Fiction
2. Non-fiction
3. Science
4. Biography
5. Children""")
            while True:
                try:
                    genopc = int(input("Select an option: "))
                    if 1 <= genopc <= len(genre):
                        genopc -= 1
                        gen = genre[genopc]
                        print(f"\nYou selected {gen}")
                        break
                    else:
                        print("\nPlease insert a valid option\n")
                except ValueError:
                    print("Insert a valid option")
            inv = add_book(inv, nam, aut, amo, gen)
        
        #Searching a book
        case 2:
            nam = str(input("What book are you looking for: "))
            book = search(inv, nam)
            if book:
                print(f"""\n
Book founded:
Name: {book["name"]}
Author: {book["author"]}
Amount: {book["amount"]}
Genre: {book["genre"]}
Borrowed: {book["borrowed"]}""")
        
        #Listing books
        case 3:
            list_books(inv, genre)
        
        #Borrowing books
        case 4:
            nam = str(input("What book are you borrowing: "))
            book_loan(inv,nam)
        
        #Returning books
        case 5:
            nam = str(input("What book are you returning: "))
            book_return(inv, nam)
        
        #Update amount
        case 6:
            nam = str (input("What book you want to update amount: "))
            while True:
                try:
                    newamo = int(input("What's the new amount: "))
                    if newamo > 0:
                        break
                    else:
                        print("Insert a valid amount")
                except ValueError:
                    print("Insert a valid amount")
            change_amount(inv, nam, newamo)

        #Delete book
        case 7:
            nam = str(input("What book you want to delete: "))
            delete_book(inv, nam)
        #Clear inventory
        case 8:
            clear_inventory(inv)

        #Exit
        case 9:
            exit()