# ساخت یک الگوی مثلثی با کاراکترها

# تابعی برای چاپ الگوی مثلثی
def print_triangle(height):
    for i in range(1, height + 1):
        print(" " * (height - i) + "*" * (2 * i - 1))  # چاپ فضا و ستاره‌ها

# دریافت ارتفاع مثلث از کاربر
height = int(input("Enter the height of the triangle: "))

# فراخوانی تابع برای چاپ مثلث
print_triangle(height)
