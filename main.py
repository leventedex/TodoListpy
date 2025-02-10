
while True :
    user_action = input("Type: (a)dd / (s)how / (e)dit / (c)omplete / e(x)it: ")
    user_action = user_action.strip()
    match user_action:
        case 'add' | 'a':
            todo=input("Enter a todo: " + "\n")
            # read the items from file
            file = open('todos.txt', 'r')
            todos = file.readlines()
            #add the new item to the list
            todos.append(todo)
            # overwrite the file with new vaues
            file = open('todos.txt', 'w')
            file.writelines(todos)
        case 'show' | 's':
            for index, item in enumerate(todos):
                #print(f"{todos.index(item)}: {item}")
                print(f"{index}: {item.capitalize()}")
        case 'exit' | 'x':
            break
        case 'edit' | 'e':
            index = int(input("Enter the index of the todo to edit: "))
            if index < len(todos):
                print(f"Editing todo: {todos[index]}")
                new_todo = input("Enter the new todo: ")
                todos[index] = new_todo
            else:
                print("Index out of range!")
        case 'complete' | 'c':
            index = int(input("Enter the index of the todo to complete: "))
            if index < len(todos):
                print(f"Completing todo: {todos[index]}")
                todos.pop(index)
            else:
                print("Index out of range!")
        case _:
            print("This is not a valid input!")
print("Bye!")