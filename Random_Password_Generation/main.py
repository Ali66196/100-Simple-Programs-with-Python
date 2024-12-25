# تولید رمز عبور تصادفی

import random
import string

# تابعی برای تولید رمز عبور تصادفی
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation  # کاراکترهای ممکن برای رمز عبور
    password = ''.join(random.choice(characters) for _ in range(length))  # انتخاب تصادفی کاراکترها
    return password

# دریافت طول رمز عبور از کاربر
length = int(input("Enter the length of the password: "))

# فراخوانی تابع و نمایش رمز عبور تصادفی
print(f"Your random password is: {generate_password(length)}")
