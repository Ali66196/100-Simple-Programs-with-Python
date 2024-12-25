# برنامه محاسبه مساحت و محیط اشکال هندسی (دایره، مستطیل و مثلث)

import math  # برای استفاده از ثابت پی (π)

# تابعی برای محاسبه مساحت و محیط دایره
def circle_area_perimeter(radius):
    area = math.pi * radius ** 2  # مساحت دایره
    perimeter = 2 * math.pi * radius  # محیط دایره
    return area, perimeter

# تابعی برای محاسبه مساحت و محیط مستطیل
def rectangle_area_perimeter(length, width):
    area = length * width  # مساحت مستطیل
    perimeter = 2 * (length + width)  # محیط مستطیل
    return area, perimeter

# تابعی برای محاسبه مساحت و محیط مثلث
def triangle_area_perimeter(base, height, side1, side2, side3):
    area = 0.5 * base * height  # مساحت مثلث
    perimeter = side1 + side2 + side3  # محیط مثلث
    return area, perimeter

# نمایش منو برای انتخاب نوع شکل هندسی
print("Select the shape:")
print("1. Circle")
print("2. Rectangle")
print("3. Triangle")

# گرفتن ورودی از کاربر برای انتخاب نوع شکل
choice = input("Enter choice (1/2/3): ")

# انجام محاسبات بر اساس انتخاب کاربر
if choice == '1':
    radius = float(input("Enter the radius of the circle: "))  # دریافت شعاع دایره
    area, perimeter = circle_area_perimeter(radius)  # فراخوانی تابع دایره
    print(f"Area of the circle: {area:.2f}")
    print(f"Perimeter of the circle: {perimeter:.2f}")
elif choice == '2':
    length = float(input("Enter the length of the rectangle: "))  # دریافت طول مستطیل
    width = float(input("Enter the width of the rectangle: "))  # دریافت عرض مستطیل
    area, perimeter = rectangle_area_perimeter(length, width)  # فراخوانی تابع مستطیل
    print(f"Area of the rectangle: {area:.2f}")
    print(f"Perimeter of the rectangle: {perimeter:.2f}")
elif choice == '3':
    base = float(input("Enter the base of the triangle: "))  # دریافت قاعده مثلث
    height = float(input("Enter the height of the triangle: "))  # دریافت ارتفاع مثلث
    side1 = float(input("Enter the length of side 1 of the triangle: "))  # دریافت ضلع اول مثلث
    side2 = float(input("Enter the length of side 2 of the triangle: "))  # دریافت ضلع دوم مثلث
    side3 = float(input("Enter the length of side 3 of the triangle: "))  # دریافت ضلع سوم مثلث
    area, perimeter = triangle_area_perimeter(base, height, side1, side2, side3)  # فراخوانی تابع مثلث
    print(f"Area of the triangle: {area:.2f}")
    print(f"Perimeter of the triangle: {perimeter:.2f}")
else:
    print("Invalid input! Please choose a valid shape.")
