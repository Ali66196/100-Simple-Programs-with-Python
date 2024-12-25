# برنامه ایجاد یک لیست از اعداد تصادفی

import random  # وارد کردن کتابخانه random برای تولید اعداد تصادفی

# تابعی برای ایجاد یک لیست از اعداد تصادفی
def generate_random_list(size, lower, upper):
    return [random.randint(lower, upper) for _ in range(size)]  # ایجاد لیستی با اندازه مشخص و اعداد تصادفی بین lower و upper

# گرفتن ورودی از کاربر برای اندازه لیست و محدوده اعداد
size = int(input("Enter the size of the list: "))  # دریافت اندازه لیست از کاربر
lower = int(input("Enter the lower bound of the numbers: "))  # دریافت محدوده پایین اعداد
upper = int(input("Enter the upper bound of the numbers: "))  # دریافت محدوده بالا اعداد

# فراخوانی تابع و نمایش لیست تصادفی
random_list = generate_random_list(size, lower, upper)  # فراخوانی تابع تولید لیست تصادفی
print(f"The random list is: {random_list}")
