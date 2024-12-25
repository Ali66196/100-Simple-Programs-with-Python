# محاسبه حقوق کارکنان ساده

# تابع برای محاسبه حقوق
def calculate_salary(hours_worked, hourly_rate):
    return hours_worked * hourly_rate

# دریافت اطلاعات کارکنان
employee_name = input("Enter employee's name: ")
hours_worked = float(input(f"Enter {employee_name}'s worked hours: "))
hourly_rate = float(input(f"Enter {employee_name}'s hourly rate: "))

# محاسبه حقوق و نمایش نتیجه
salary = calculate_salary(hours_worked, hourly_rate)
print(f"{employee_name}'s salary is: {salary}")
