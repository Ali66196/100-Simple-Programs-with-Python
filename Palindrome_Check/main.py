# برنامه بررسی Palindrome بودن یک رشته

# تابعی برای بررسی اینکه رشته پالیندروم است یا نه
def is_palindrome(string):
    return string == string[::-1]  # بررسی معکوس بودن رشته با خود آن

# گرفتن ورودی از کاربر برای وارد کردن رشته
text = input("Enter a string: ")  # دریافت رشته از کاربر

# فراخوانی تابع و نمایش نتیجه
if is_palindrome(text):
    print(f"'{text}' is a palindrome.")
else:
    print(f"'{text}' is not a palindrome.")
