# برنامه ساده تفریق دو عدد

# تابعی برای تفریق دو عدد
def subtract_numbers(a, b):
    return a - b

# گرفتن ورودی از کاربر
num1 = float(input("Enter the first number: "))  # دریافت عدد اول از کاربر
num2 = float(input("Enter the second number: "))  # دریافت عدد دوم از کاربر

# فراخوانی تابع تفریق و نمایش نتیجه
result = subtract_numbers(num1, num2)  # فراخوانی تابع تفریق
print(f"The result of subtracting {num2} from {num1} is: {result}")  # نمایش نتیجه تفریق
