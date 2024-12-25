# محاسبه توان اعداد

# تابع برای محاسبه توان یک عدد
def power(base, exponent):
    return base ** exponent

# دریافت ورودی از کاربر
base = float(input("Enter the base number: "))
exponent = int(input("Enter the exponent: "))

# نمایش نتیجه
result = power(base, exponent)
print(f"{base} raised to the power of {exponent} is {result}")
