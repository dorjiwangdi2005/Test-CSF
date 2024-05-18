# initialize empty lists, set, and dictionary
book_list = []
book_set = set()
book_dict = {}

#adding a book 
book_list.append ("python program")
book_set.add ("John Smith")
book_dict ["python program"] = "John Smith"

book_list.append ("data structure")
book_set.add ("dorji wangdi")
book_dict ["data structure "] = "dorji wangdi"

book_list.append ("data statices")
book_set.add ("Tashi Pelden")
book_dict ["data statices"] = "Tashi Pelden"

# searching for a book 
search_title = input("enter the title of the book in the search: ") .lower()
if search_title in book_list: 
    print ("book title: ", search_title)
    print (f"book found! author: {book_dict[search_title]}" )
else: 
    print ("book not found")

#display all books
print("list of the books:")
for book in book_list:
    print(book)

# removing a book 
remove_title = input ("enter the title of the book to remove ar else enter to skip: ")
if remove_title in book_list: 
    remove_author = book_list[remove_title]
    books_list.remove (remove_title)
    authors_set.remove (remove_author)
    del books_dict[remove_title]
    
    print ("Book remove successfully!")
    print("Books available: ", book_list)

else: 
    print("Book not found!")
