# برنامه مرتب‌سازی یک لیست اعداد

# تابعی برای مرتب‌سازی یک لیست اعداد به ترتیب صعودی
def sort_list(numbers):
    return sorted(numbers)  # استفاده از تابع sorted برای مرتب‌سازی لیست

# گرفتن ورودی از کاربر برای وارد کردن لیست اعداد
numbers_input = input("Enter numbers separated by spaces: ")  # دریافت اعداد از کاربر
numbers = [int(num) for num in numbers_input.split()]  # تبدیل ورودی به لیست اعداد

# فراخوانی تابع و نمایش لیست مرتب‌شده
sorted_numbers = sort_list(numbers)  # فراخوانی تابع مرتب‌سازی
print(f"Sorted list: {sorted_numbers}")
