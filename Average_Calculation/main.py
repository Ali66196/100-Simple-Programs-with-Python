# برنامه محاسبه میانگین لیست اعداد

# تابعی برای محاسبه میانگین لیست اعداد
def calculate_average(numbers):
    return sum(numbers) / len(numbers)  # محاسبه میانگین با تقسیم مجموع اعداد بر تعداد آن‌ها

# گرفتن ورودی از کاربر برای وارد کردن لیست اعداد
numbers_input = input("Enter numbers separated by spaces: ")  # دریافت اعداد از کاربر
numbers = [int(num) for num in numbers_input.split()]  # تبدیل ورودی به لیست اعداد

# فراخوانی تابع و نمایش میانگین
average = calculate_average(numbers)  # فراخوانی تابع محاسبه میانگین
print(f"The average of the list is: {average}")
