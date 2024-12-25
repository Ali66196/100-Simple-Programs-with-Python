# رسم نمودار با کتابخانه matplotlib

import matplotlib.pyplot as plt

# داده‌های نمونه برای رسم نمودار
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# رسم نمودار
plt.plot(x, y, label="x^2", color='blue', marker='o')

# تنظیمات نمودار
plt.title("Sample Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()

# نمایش نمودار
plt.show()
