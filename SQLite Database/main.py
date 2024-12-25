# ذخیره داده‌ها در دیتابیس SQLite

import sqlite3  # وارد کردن کتابخانه sqlite3 برای ارتباط با دیتابیس SQLite

# تابع برای ایجاد دیتابیس و جدول
def create_database():
    conn = sqlite3.connect("tasks.db")  # اتصال به دیتابیس (ایجاد آن در صورت نبود)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (
                        id INTEGER PRIMARY KEY,
                        task_name TEXT NOT NULL,
                        completed BOOLEAN NOT NULL)''')
    conn.commit()
    conn.close()

# تابع برای ذخیره یک کار در دیتابیس
def save_task(task_name, completed=False):
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (task_name, completed) VALUES (?, ?)", (task_name, completed))
    conn.commit()
    conn.close()

# تابع برای نمایش وظایف از دیتابیس
def show_tasks():
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    for task in tasks:
        print(f"Task: {task[1]}, Completed: {task[2]}")
    conn.close()

# ایجاد دیتابیس و جدول
create_database()

# ذخیره یک کار در دیتابیس
save_task("Learn Python")
save_task("Complete homework", completed=True)

# نمایش وظایف
show_tasks()
