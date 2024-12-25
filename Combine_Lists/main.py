# برنامه ترکیب دو لیست

# تابعی برای ترکیب دو لیست
def combine_lists(list1, list2):
    return list1 + list2  # استفاده از عملگر + برای ترکیب دو لیست

# گرفتن ورودی از کاربر برای وارد کردن دو لیست
list1_input = input("Enter the first list of numbers separated by spaces: ")  # دریافت لیست اول
list2_input = input("Enter the second list of numbers separated by spaces: ")  # دریافت لیست دوم

# تبدیل ورودی‌ها به لیست‌های اعداد
list1 = [int(num) for num in list1_input.split()]
list2 = [int(num) for num in list2_input.split()]

# فراخوانی تابع و نمایش لیست ترکیب شده
combined_list = combine_lists(list1, list2)  # فراخوانی تابع ترکیب دو لیست
print(f"The combined list is: {combined_list}")
