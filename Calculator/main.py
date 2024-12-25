# برنامه ماشین حساب ساده

# تابع برای جمع دو عدد
def add_numbers(a, b):
    return a + b

# تابع برای تفریق دو عدد
def subtract_numbers(a, b):
    return a - b

# تابع برای ضرب دو عدد
def multiply_numbers(a, b):
    return a * b

# تابع برای تقسیم دو عدد
def divide_numbers(a, b):
    if b != 0:  # بررسی تقسیم بر صفر
        return a / b
    else:
        return "Error! Division by zero."  # پیغام خطا در صورت تقسیم بر صفر

# نمایش منو برای انتخاب عملیات
print("Select operation:")
print("1. Add (+)")
print("2. Subtract (-)")
print("3. Multiply (*)")
print("4. Divide (/)")

# گرفتن ورودی از کاربر برای انتخاب عملیات
choice = input("Enter choice (1/2/3/4): ")

# گرفتن ورودی دو عدد از کاربر
num1 = float(input("Enter the first number: "))  # دریافت عدد اول
num2 = float(input("Enter the second number: "))  # دریافت عدد دوم

# انجام عملیات بر اساس انتخاب کاربر و نمایش نتیجه
if choice == '1':
    result = add_numbers(num1, num2)
    print(f"The result of adding {num1} and {num2} is: {result}")
elif choice == '2':
    result = subtract_numbers(num1, num2)
    print(f"The result of subtracting {num2} from {num1} is: {result}")
elif choice == '3':
    result = multiply_numbers(num1, num2)
    print(f"The result of multiplying {num1} and {num2} is: {result}")
elif choice == '4':
    result = divide_numbers(num1, num2)
    print(f"The result of dividing {num1} by {num2} is: {result}")
else:
    print("Invalid input! Please choose a valid operation.")
