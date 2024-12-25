# سیستم یادآوری وظایف

# دیکشنری برای ذخیره وظایف و وضعیت انجام‌شدن آنها
tasks = {}

# تابعی برای افزودن وظیفه جدید
def add_task(task_name):
    tasks[task_name] = False  # وضعیت انجام نشده

# تابعی برای نشان دادن وظایف
def show_tasks():
    if tasks:
        print("\nTask List:")
        for task, status in tasks.items():
            status_text = "Not Done" if not status else "Done"
            print(f"{task}: {status_text}")
    else:
        print("\nNo tasks found.")

# تابعی برای علامت‌گذاری وظیفه به‌عنوان انجام‌شده
def mark_task_done(task_name):
    if task_name in tasks:
        tasks[task_name] = True
    else:
        print("This task does not exist.")

# تابع اصلی برنامه که از کاربر ورودی می‌گیرد
def task_reminder_system():
    while True:
        print("\nTask Reminder System")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark Task as Done")
        print("4. Exit")

        choice = input("Please choose an option: ")

        if choice == "1":
            task_name = input("Enter task name: ")
            add_task(task_name)
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            task_name = input("Enter the task name to mark as done: ")
            mark_task_done(task_name)
        elif choice == "4":
            print("Exiting the program...")
            break
        else:
            print("Please enter a valid option.")

# اجرای سیستم یادآوری وظایف
task_reminder_system()
