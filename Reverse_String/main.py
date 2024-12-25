# برنامه معکوس کردن یک رشته

# تابعی برای معکوس کردن رشته
def reverse_string(string):
    return string[::-1]  # استفاده از تکنیک اسلایس برای معکوس کردن رشته

# گرفتن ورودی از کاربر برای وارد کردن رشته
text = input("Enter a string: ")  # دریافت رشته از کاربر

# فراخوانی تابع و نمایش رشته معکوس شده
reversed_text = reverse_string(text)  # فراخوانی تابع معکوس کردن رشته
print(f"The reversed string is: {reversed_text}")
