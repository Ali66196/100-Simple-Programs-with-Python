# محاسبه سن کاربر بر اساس تاریخ تولد

from datetime import datetime

# تابعی برای محاسبه سن
def calculate_age(birthdate):
    today = datetime.today()  # تاریخ امروز
    age = today.year - birthdate.year  # محاسبه سن
    if today.month < birthdate.month or (today.month == birthdate.month and today.day < birthdate.day):
        age -= 1  # اگر تاریخ تولد هنوز نرسیده باشد یک سال از سن کم می‌شود
    return age

# دریافت تاریخ تولد از کاربر
birthdate_input = input("Enter your birthdate (YYYY-MM-DD): ")
birthdate = datetime.strptime(birthdate_input, "%Y-%m-%d")  # تبدیل ورودی به شیء تاریخ

# محاسبه سن و نمایش آن
age = calculate_age(birthdate)
print(f"You are {age} years old.")
