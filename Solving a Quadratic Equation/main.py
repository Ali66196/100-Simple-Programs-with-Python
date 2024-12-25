# حل معادله درجه دوم (ax^2 + bx + c = 0)

import cmath  # برای کار با اعداد مختلط

# تابع برای حل معادله درجه دوم
def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c  # محاسبه دلتای معادله
    root1 = (-b + cmath.sqrt(discriminant)) / (2*a)  # ریشه اول
    root2 = (-b - cmath.sqrt(discriminant)) / (2*a)  # ریشه دوم
    return root1, root2

# دریافت ضرایب معادله از کاربر
a = float(input("لطفاً ضریب a را وارد کنید: "))
b = float(input("لطفاً ضریب b را وارد کنید: "))
c = float(input("لطفاً ضریب c را وارد کنید: "))

# حل معادله
root1, root2 = solve_quadratic(a, b, c)

# نمایش نتایج
print(f"ریشه‌های معادله درجه دوم: {root1} و {root2}")
