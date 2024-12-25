# محاسبه میانگین معدل دانش‌آموزان

# لیست دانش‌آموزان و معدل‌های آنها
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78},
    {"name": "David", "grade": 88}
]

# تابع برای محاسبه میانگین معدل‌ها
def calculate_average(students):
    total_grades = sum(student["grade"] for student in students)
    average_grade = total_grades / len(students)
    return average_grade

# محاسبه و نمایش میانگین معدل
average = calculate_average(students)
print(f"The average grade of students is: {average:.2f}")
