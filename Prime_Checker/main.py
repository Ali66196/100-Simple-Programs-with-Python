# برنامه بررسی عدد اول بودن یک عدد

# تابعی برای بررسی اول بودن یک عدد
def is_prime(number):
    if number <= 1:  # اعداد کمتر یا مساوی 1 عدد اول نیستند
        return False
    for i in range(2, int(number ** 0.5) + 1):  # بررسی از 2 تا ریشه مربع عدد
        if number % i == 0:  # اگر عدد بر i بخش‌پذیر باشد
            return False
    return True  # در غیر این صورت عدد اول است

# گرفتن ورودی از کاربر برای وارد کردن عدد
num = int(input("Enter a number: "))  # دریافت عدد از کاربر

# فراخوانی تابع و نمایش نتیجه
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
