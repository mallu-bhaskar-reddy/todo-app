import sys
todos = []
while True:
    user_action = input("Type add or show or exit: ")
    user_action = user_action.strip()
    match user_action:
        case 'add':
            todo = input("Enter todo: ")
            todos.append(todo)
        case 'show' | 'display':
            for item in todos:
                item = item.title()
                print(item)
        case 'exit':
            sys.exit()
        case _:
            print("Hey, you entered an unknown command")

