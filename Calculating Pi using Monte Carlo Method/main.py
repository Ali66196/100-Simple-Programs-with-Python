# محاسبه عدد π با استفاده از روش Monte Carlo

import random

# تابع برای محاسبه Pi با روش Monte Carlo
def estimate_pi(num_samples):
    inside_circle = 0
    for _ in range(num_samples):
        x, y = random.uniform(-1, 1), random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            inside_circle += 1
    return (inside_circle / num_samples) * 4

# دریافت تعداد نمونه‌ها از کاربر
num_samples = int(input("تعداد نمونه‌ها را وارد کنید: "))

# محاسبه Pi
pi_estimate = estimate_pi(num_samples)

# نمایش نتیجه
print(f"برآورد عدد Pi با {num_samples} نمونه: {pi_estimate}")
