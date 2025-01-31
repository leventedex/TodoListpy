user_prompt = "Enter todo:\" "
todos = []
while True :
    todo = input(user_prompt)
    print(todo.capitalize())
    todos.append(todo)
    print(todos)