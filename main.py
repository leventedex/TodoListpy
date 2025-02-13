#Check if file exists and crerate one if it does not
import os
file = 'todos.txt'
#file full path: 
#open(r"C:\Users\user\Documents\Python\TodoListpy\todos.txt", 'w')
#r"" is used to escape the backslash it means raw string
if not os.path.exists(file):
    with open(file, 'w') as f:
        f.write('')
        print(f"File {os.path.abspath(file)} created!")
        f.close()

while True :
    user_action = input("Type: add / show / edit / complete / exit: ")
    user_action = user_action.strip()
    if 'add' in user_action:
        todo=user_action[4:]
        # read the items from file
        # file = open('todos.txt', 'r')
        # todos = file.readlines()
        # file.close()

        #A better way to open file in read mode and close it automatically
        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        #add the new item to the list
        todos.append(todo)
        # overwrite the file with new vaues
        with open('todos.txt', 'w') as file:
            file.writelines(todos)
            
    elif 'show' in user_action:
        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        #Create a new with the new modified items:
        #new_todos = []
        #for item in todos:
        #    new_item = item.strip('\n')
        #    new_todos.append(new_item)

        #list comprehension:
        #new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            #print(f"{todos.index(item)}: {item}")
            item=item.strip('\n')
            print(f"{index}: {item.capitalize()}")
    elif 'exit' in user_action:
        break
    elif 'edit'in user_action:
        #index = int(input("Enter the index of the todo to edit: "))
        index = int(user_action[5:])
        with open('todos.txt', 'r') as file:
            todos = file.readlines()
        if index < len(todos):
            print(f"Editing todo: {todos[index].strip("\n")}")
            new_todo = input("Enter the new todo: ")
            todos[index] = new_todo + '\n'
            #overwrite the file with new values
            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        else:
            print("Index out of range!")
    elif 'complete' in user_action:
        #index = int(input("Enter the index of the todo to complete: "))
        index = int(user_action[9:])
        #Build list from the file
        with open('todos.txt', 'r') as file:
            todos = file.readlines()
        if index < len(todos):
            print(f"Completing todo: {todos[index].strip("\n")}")
            todos.pop(index)
            #overwrite the file with new values
            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        else:
            print("Index out of range!")
    else:
        print("Invalid action!")
        
print("Bye!")