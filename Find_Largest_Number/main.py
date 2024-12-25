# برنامه پیدا کردن بزرگ‌ترین عدد در یک لیست

# تابعی برای پیدا کردن بزرگ‌ترین عدد در لیست
def find_largest(numbers):
    return max(numbers)  # استفاده از تابع max برای پیدا کردن بزرگ‌ترین عدد در لیست

# گرفتن ورودی از کاربر برای وارد کردن لیست اعداد
numbers_input = input("Enter numbers separated by spaces: ")  # دریافت اعداد از کاربر
numbers = [int(num) for num in numbers_input.split()]  # تبدیل ورودی به لیست اعداد

# فراخوانی تابع و نمایش بزرگ‌ترین عدد
largest_number = find_largest(numbers)  # فراخوانی تابع پیدا کردن بزرگ‌ترین عدد
print(f"The largest number in the list is: {largest_number}")
