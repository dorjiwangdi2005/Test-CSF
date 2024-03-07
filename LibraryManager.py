book_list = []
book_set = set()
book_dict = {}

book_list.append ("python program")
book_set.add ("John Smith")
book_dict ["python program"] = "John Smith"

book_list.append ("data structure")
book_set.add ("dorji wangdi")
book_dict ["data structure "] = "dorji wangdi"

book_list.append ("data statices")
book_set.add ("Tashi Pelden")
book_dict ["data statices"] = "Tashi Pelden"

search_title = input("enter the title of the book in the search: ") .lower()
if search_title in book_list: 
    print ("book title: ", search_title)
    print (f"book found! author: {book_dict[search_title]}" )
else: 
    print ("book not found")

