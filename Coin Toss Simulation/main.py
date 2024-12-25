# شبیه‌سازی پرتاب سکه

import random

# تابع برای شبیه‌سازی پرتاب سکه
def coin_toss():
    return "Heads" if random.random() < 0.5 else "Tails"

# دریافت تعداد پرتاب‌ها از کاربر
num_tosses = int(input("تعداد پرتاب‌ها را وارد کنید: "))

# شبیه‌سازی پرتاب سکه
results = {"Heads": 0, "Tails": 0}
for _ in range(num_tosses):
    result = coin_toss()
    results[result] += 1

# نمایش نتایج
print(f"نتایج پرتاب سکه: \nHeads: {results['Heads']} \nTails: {results['Tails']}")
