from queue import LifoQueue

backward_history = LifoQueue()
forward_history = LifoQueue()
current_page = None

NO_of_visits = int(input("enter the number of URL history: "))

print ("enter URLs to visit: ")
for i in range (NO_of_visits):

    url = input("URL:")
    print(f"Visiting {url}")
    backward_history.put(current_page)
    current_page = url

print (f'current page: {current_page}')

#go back
while input("Do you want to go back? (yes/no: )").lower() == 'yes':
    if not forward_history.empty():
        forward_history.put(current_page)
        current_page = backword_history.get()
    else: 
        print("no previous page available ")

# go forward 
while input ('Do you want to go forwad? (yes/no): ').lower()== 'yes:':
    if not forward_history.empty():
        backward_history.put(current_page)
        current_page = forward_history.get()
        print(f'Going to {current_page}')
    else: 
        print('No forward page available')
