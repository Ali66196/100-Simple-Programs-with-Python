# برنامه شمارش تکرار یک مقدار در لیست

# تابعی برای شمارش تکرار یک مقدار در لیست
def count_occurrences(numbers, target):
    return numbers.count(target)  # استفاده از متد count برای شمارش تعداد تکرارها

# گرفتن ورودی از کاربر برای وارد کردن لیست و عدد مورد نظر
numbers_input = input("Enter numbers separated by spaces: ")  # دریافت لیست اعداد از کاربر
numbers = [int(num) for num in numbers_input.split()]  # تبدیل ورودی به لیست اعداد
target = int(input("Enter the number you want to count: "))  # دریافت عدد مورد نظر برای شمارش تکرارها

# فراخوانی تابع و نمایش تعداد تکرارهای عدد
occurrences = count_occurrences(numbers, target)  # فراخوانی تابع شمارش تکرارها
print(f"The number {target} appears {occurrences} times in the list.")
