# برنامه تبدیل دما (سلسیوس به فارنهایت و برعکس)

# تابع برای تبدیل سلسیوس به فارنهایت
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# تابع برای تبدیل فارنهایت به سلسیوس
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# نمایش منو برای انتخاب تبدیل دما
print("Select temperature conversion:")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

# گرفتن ورودی از کاربر برای انتخاب تبدیل دما
choice = input("Enter choice (1/2): ")

# انجام تبدیل دما بر اساس انتخاب کاربر
if choice == '1':
    celsius = float(input("Enter the temperature in Celsius: "))  # دریافت دما به سلسیوس
    result = celsius_to_fahrenheit(celsius)  # فراخوانی تابع تبدیل سلسیوس به فارنهایت
    print(f"{celsius}°C is equal to {result:.2f}°F.")
elif choice == '2':
    fahrenheit = float(input("Enter the temperature in Fahrenheit: "))  # دریافت دما به فارنهایت
    result = fahrenheit_to_celsius(fahrenheit)  # فراخوانی تابع تبدیل فارنهایت به سلسیوس
    print(f"{fahrenheit}°F is equal to {result:.2f}°C.")
else:
    print("Invalid input! Please choose a valid conversion type.")
