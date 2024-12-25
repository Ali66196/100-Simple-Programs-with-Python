# برنامه ساده جمع دو عدد

# تابعی برای جمع دو عدد
def add_numbers(a, b):
    return a + b

# گرفتن ورودی از کاربر
num1 = float(input("Enter the first number: "))  # دریافت عدد اول از کاربر
num2 = float(input("Enter the second number: "))  # دریافت عدد دوم از کاربر

# فراخوانی تابع جمع و نمایش نتیجه
result = add_numbers(num1, num2)  # فراخوانی تابع جمع
print(f"The result of adding {num1} and {num2} is: {result}")  # نمایش نتیجه جمع
