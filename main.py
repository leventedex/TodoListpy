todos = []
while True :
    user_action = input("Type (a)dd / (s)how / e(x)it: ")
    user_action = user_action.strip()
    match user_action:
        case 'add' | 'a':
            todo=input("Enter a todo: ")
            todos.append(todo)
        case 'show' | 's':
            for item in todos:
                print(item)
        case 'exit' | 'x':
            break
        case _:
            print("This is not a valid input!")
print("Bye!")