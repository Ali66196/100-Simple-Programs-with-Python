# مدیریت لیست دانش‌آموزان

# لیست دانش‌آموزان
students = []

# تابع برای افزودن دانش‌آموز
def add_student(name, grade):
    students.append({"name": name, "grade": grade})
    print(f"Student {name} has been added.")

# تابع برای نمایش لیست دانش‌آموزان
def show_students():
    print("List of students:")
    for student in students:
        print(f"Name: {student['name']}, Grade: {student['grade']}")

# افزودن دانش‌آموز به لیست
add_student("Alice", 85)
add_student("Bob", 92)

# نمایش لیست دانش‌آموزان
show_students()
