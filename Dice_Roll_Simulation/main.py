# شبیه‌سازی پرتاب تاس

import random  # وارد کردن کتابخانه random برای پرتاب تصادفی

# تابعی برای شبیه‌سازی پرتاب تاس
def roll_dice():
    return random.randint(1, 6)  # انتخاب عدد تصادفی بین 1 تا 6

# گرفتن تعداد پرتاب‌ها از کاربر
num_rolls = int(input("How many times do you want to roll the dice? "))

# پرتاب تاس‌ها و نمایش نتایج
for _ in range(num_rolls):
    print(f"Rolled: {roll_dice()}")
