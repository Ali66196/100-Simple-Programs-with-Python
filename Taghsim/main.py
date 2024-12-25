# برنامه ساده تقسیم دو عدد

# تابعی برای تقسیم دو عدد
def divide_numbers(a, b):
    if b != 0:  # بررسی تقسیم بر صفر
        return a / b
    else:
        return "Error! Division by zero."  # پیغام خطا در صورت تقسیم بر صفر

# گرفتن ورودی از کاربر
num1 = float(input("Enter the first number: "))  # دریافت عدد اول از کاربر
num2 = float(input("Enter the second number: "))  # دریافت عدد دوم از کاربر

# فراخوانی تابع تقسیم و نمایش نتیجه
result = divide_numbers(num1, num2)  # فراخوانی تابع تقسیم
print(f"The result of dividing {num1} by {num2} is: {result}")  # نمایش نتیجه تقسیم
