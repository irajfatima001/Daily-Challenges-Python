tasks = []  

while True:
    print("\n📌 To-Do List:")
    print("1️⃣ Add Task")
    print("2️⃣ Show Tasks")
    print("3️⃣ Delete Task")
    print("4️⃣ Exit")
    
    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter new task: ").strip()
        if task:
            tasks.append(task)
            print(f"✅ Task Added: {task}")
        else:
            print("⚠ Task cannot be empty!")

    elif choice == "2":
        if tasks:
            print("\n📋 Your Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
        else:
            print("📭 No tasks available!")

    elif choice == "3":
        if tasks:
            try:
                task_no = int(input("Enter task number to delete: "))
                if 1 <= task_no <= len(tasks):
                    removed_task = tasks.pop(task_no - 1)
                    print(f"❌ Task Deleted: {removed_task}")
                else:
                    print("⚠ Invalid task number!")
            except ValueError:
                print("⚠ Please enter a valid number!")
        else:
            print("📭 No tasks to delete!")

    elif choice == "4":
        print("👋 Exiting To-Do List. Have a great day!")
        break

    else:
        print("⚠ Invalid choice! Please select 1-4.")
