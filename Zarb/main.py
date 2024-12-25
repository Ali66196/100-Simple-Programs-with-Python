# برنامه ساده ضرب دو عدد

# تابعی برای ضرب دو عدد
def multiply_numbers(a, b):
    return a * b

# گرفتن ورودی از کاربر
num1 = float(input("Enter the first number: "))  # دریافت عدد اول از کاربر
num2 = float(input("Enter the second number: "))  # دریافت عدد دوم از کاربر

# فراخوانی تابع ضرب و نمایش نتیجه
result = multiply_numbers(num1, num2)  # فراخوانی تابع ضرب
print(f"The result of multiplying {num1} and {num2} is: {result}")  # نمایش نتیجه ضرب
