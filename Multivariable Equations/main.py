# حل معادلات چند مجهولی ساده

import sympy as sp  # وارد کردن کتابخانه sympy برای حل معادلات

# تعریف متغیرها
x, y = sp.symbols('x y')

# تعریف معادلات
eq1 = sp.Eq(x + y, 10)
eq2 = sp.Eq(2*x - y, 5)

# حل معادلات
solutions = sp.solve((eq1, eq2), (x, y))

# نمایش پاسخ‌ها
print(f"Solution: x = {solutions[x]}, y = {solutions[y]}")
