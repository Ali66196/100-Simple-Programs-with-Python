# محاسبه فاکتوریل عدد

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

# دریافت عدد از کاربر
number = int(input("لطفاً عددی وارد کنید تا فاکتوریل آن محاسبه شود: "))

# محاسبه و نمایش فاکتوریل
print(f"فاکتوریل {number} برابر است با: {factorial(number)}")
