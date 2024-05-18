from queue import LifoQueue
backword_history = LifoQueue()
forward_history = LifoQueue()
current_page = None 

#visit funtion 
NoOfVisists = int(input("enter the number of url history: "))

print("enter URLs to visit:")
for i in range(NoOfVisists):
    url = input("URL: ")
    print(f"Visiting {url}")
    backword_history.put(current_page)
    current_page = url

# display current page 
print(f"Current page: {current_page}")

#go back
while input("Do you want to go back? (yes/no): ").lower()== "yes":
    if not backword_history.empty():
        forward_history.put(current_page)
        current_page = backword_history.get()
        print(f"Going back to {current_page}")
    else: 
        print("No previous page avaliable" )

# go forward 
while input ("Do you want to go forward? (yes/no): ").lower() == 'yes':
    if not forward_history.empty():
        backword_history.put(current_page)
        current_page = forward_history
        print(f"Going forward to {current_page}")
    else:
        print("No forward page available")
