# ساخت یک الگوی الماس شکل

# تابعی برای چاپ الگوی الماس
def print_diamond(height):
    # چاپ نیمه بالایی الماس
    for i in range(1, height + 1):
        print(" " * (height - i) + "*" * (2 * i - 1))
    
    # چاپ نیمه پایینی الماس
    for i in range(height - 1, 0, -1):
        print(" " * (height - i) + "*" * (2 * i - 1))

# دریافت ارتفاع از کاربر
height = int(input("Enter the height of the diamond: "))

# فراخوانی تابع برای چاپ الماس
print_diamond(height)
