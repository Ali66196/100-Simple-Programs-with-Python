# ایجاد یک چک‌لیست روزانه

# دیکشنری برای ذخیره وظایف روزانه
tasks = {
    "Task 1": False,
    "Task 2": False,
    "Task 3": False,
    "Task 4": False,
}

# تابع برای نمایش وضعیت چک‌لیست
def show_checklist():
    print("\nDaily Checklist:")
    for task, completed in tasks.items():
        status = "Completed" if completed else "Not Completed"
        print(f"{task}: {status}")

# تابع برای انجام یک کار و تغییر وضعیت آن
def complete_task(task_name):
    if task_name in tasks:
        tasks[task_name] = True
        print(f"{task_name} marked as completed.")
    else:
        print("Task not found.")

# نمایش چک‌لیست
show_checklist()

# دریافت ورودی از کاربر برای انجام یک کار
task_name = input("\nEnter the task name to mark as completed: ")
complete_task(task_name)

# نمایش چک‌لیست پس از انجام تغییرات
show_checklist()
