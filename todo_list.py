# todo_list.py

tasks = []

def show_menu():
    print("\n💖 Neeru's To-Do List 💖")
    print("1️⃣ Add Task")
    print("2️⃣ View Tasks")
    print("3️⃣ Delete Task")
    print("4️⃣ Exit")

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"✅ '{task}' has been added to your list!")

def view_tasks():
    if not tasks:
        print("🪶 Your to-do list is empty.")
    else:
        print("\n📋 Your Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def delete_task():
    view_tasks()
    if tasks:
        try:
            task_no = int(input("Enter task number to delete: "))
            removed = tasks.pop(task_no - 1)
            print(f"🗑️ '{removed}' has been removed!")
        except (ValueError, IndexError):
            print("⚠️ Invalid task number!")

while True:
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        delete_task()
    elif choice == '4':
        print("👋 Goodbye, Neeru Naidu! Keep being productive 💪")
        break
    else:
        print("❌ Invalid choice! Please enter 1-4.")
