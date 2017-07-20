# make a list to hold onto our items
to_do = []




def show_help():
# print out instructions on how to use the app
  print("What could we do today?")
  print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help.
Enter 'SHOW' to see your current list.
""")
  
def show_list():  
  # print out the list
    print("Here's your list:")
    
    for item in to_do:
      print(item)

def add_to_list(new_item):    
# add new item to our list   
    to_do.append(new_item)
    print("Added {}. To Do List now has {} items.".format(new_item, len(to_do)))

show_help()
while True:
    # ask for new items
    new_item = input("> ")
    # be able to quit the app
    if new_item == 'DONE':
        break
    elif new_item == 'HELP':
        show_help()
        continue
    elif new_item in to_do:
      print("{} - I already have this to do".format(new_item))
      continue
      
    elif new_item == 'SHOW':
        show_list()
        continue
    add_to_list(new_item)

show_list()










