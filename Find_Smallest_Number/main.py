# برنامه پیدا کردن کوچک‌ترین عدد در یک لیست

# تابعی برای پیدا کردن کوچک‌ترین عدد در لیست
def find_smallest(numbers):
    return min(numbers)  # استفاده از تابع min برای پیدا کردن کوچک‌ترین عدد در لیست

# گرفتن ورودی از کاربر برای وارد کردن لیست اعداد
numbers_input = input("Enter numbers separated by spaces: ")  # دریافت اعداد از کاربر
numbers = [int(num) for num in numbers_input.split()]  # تبدیل ورودی به لیست اعداد

# فراخوانی تابع و نمایش کوچک‌ترین عدد
smallest_number = find_smallest(numbers)  # فراخوانی تابع پیدا کردن کوچک‌ترین عدد
print(f"The smallest number in the list is: {smallest_number}")
