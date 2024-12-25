# برنامه تبدیل واحد (سانتی‌متر به اینچ و برعکس)

# تابع برای تبدیل سانتی‌متر به اینچ
def cm_to_inch(cm):
    return cm / 2.54

# تابع برای تبدیل اینچ به سانتی‌متر
def inch_to_cm(inch):
    return inch * 2.54

# نمایش منو برای انتخاب تبدیل واحد
print("Select conversion type:")
print("1. Centimeter to Inch")
print("2. Inch to Centimeter")

# گرفتن ورودی از کاربر برای انتخاب تبدیل واحد
choice = input("Enter choice (1/2): ")

# انجام تبدیل واحد بر اساس انتخاب کاربر
if choice == '1':
    cm = float(input("Enter the length in centimeters: "))  # دریافت طول به سانتی‌متر
    result = cm_to_inch(cm)  # فراخوانی تابع تبدیل سانتی‌متر به اینچ
    print(f"{cm} centimeters is equal to {result:.2f} inches.")
elif choice == '2':
    inch = float(input("Enter the length in inches: "))  # دریافت طول به اینچ
    result = inch_to_cm(inch)  # فراخوانی تابع تبدیل اینچ به سانتی‌متر
    print(f"{inch} inches is equal to {result:.2f} centimeters.")
else:
    print("Invalid input! Please choose a valid conversion type.")
