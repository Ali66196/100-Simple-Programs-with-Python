# محاسبه فاصله دو نقطه در فضای دو بعدی

import math

# تابع برای محاسبه فاصله دو نقطه
def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# دریافت مختصات دو نقطه از کاربر
x1, y1 = map(float, input("مختصات نقطه اول را وارد کنید (x1 y1): ").split())
x2, y2 = map(float, input("مختصات نقطه دوم را وارد کنید (x2 y2): ").split())

# محاسبه فاصله و نمایش نتیجه
distance = calculate_distance(x1, y1, x2, y2)
print(f"فاصله بین دو نقطه: {distance}")
