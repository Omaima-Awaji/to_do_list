def to_do_list():
    try:
        with open("tasks.txt", "r") as file:
            tasks = [line.strip() for line in file]
    except FileNotFoundError:
        tasks = []

    while True:
        command = input('''
        1. Add task
        2. View tasks
        3. Remove task
        4. Exit
        Enter number: 
        ''')
        if command == "1":
            new_task = input("What is new on your schedule? ")
            tasks.append(new_task)
            with open("tasks.txt", "w") as file:
                for task in tasks:
                    file.write(task + "\n")
            print("Task is added!! ")

        elif command == "2":
            for index, tasks_list in enumerate(tasks, 1):
                print(f"{index}. {tasks_list}")

        elif command == "3":
            for index, tasks_list in enumerate(tasks, 1):
                print(f"{index}. {tasks_list}")
            try:
                remove_task= int(input("What task would you like to delete? Enter the number please:  "))
            except ValueError:
                print("Invalid input. Please enter a number")
                continue
            tasks.pop(remove_task - 1)
            print("Task removed successfully!")
            with open("tasks.txt", "w") as file:
                for task in tasks:
                    file.write(task + "\n")

        elif command == "4":
            break
        else:
            print("Invalid input. Please enter a number between 1 and 4.")
if __name__ == "__main__":
    to_do_list()
