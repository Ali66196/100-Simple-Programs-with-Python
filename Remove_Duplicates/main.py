# برنامه حذف اعداد تکراری از لیست

# تابعی برای حذف اعداد تکراری از لیست
def remove_duplicates(numbers):
    return list(set(numbers))  # تبدیل لیست به مجموعه (set) برای حذف تکراری‌ها و سپس بازگشت به لیست

# گرفتن ورودی از کاربر برای وارد کردن لیست اعداد
numbers_input = input("Enter numbers separated by spaces: ")  # دریافت اعداد از کاربر
numbers = [int(num) for num in numbers_input.split()]  # تبدیل ورودی به لیست اعداد

# فراخوانی تابع و نمایش لیست بدون اعداد تکراری
unique_numbers = remove_duplicates(numbers)  # فراخوانی تابع حذف اعداد تکراری
print(f"List without duplicates: {unique_numbers}")
