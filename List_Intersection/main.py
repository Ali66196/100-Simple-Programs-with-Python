# برنامه مقایسه دو لیست و پیدا کردن اشتراک آن‌ها

# تابعی برای پیدا کردن اشتراک دو لیست
def find_intersection(list1, list2):
    return list(set(list1) & set(list2))  # استفاده از عملگر & برای پیدا کردن اشتراک دو مجموعه

# گرفتن ورودی از کاربر برای وارد کردن دو لیست
list1_input = input("Enter the first list of numbers separated by spaces: ")  # دریافت لیست اول
list2_input = input("Enter the second list of numbers separated by spaces: ")  # دریافت لیست دوم

# تبدیل ورودی‌ها به لیست‌های اعداد
list1 = [int(num) for num in list1_input.split()]
list2 = [int(num) for num in list2_input.split()]

# فراخوانی تابع و نمایش اشتراک دو لیست
intersection = find_intersection(list1, list2)  # فراخوانی تابع پیدا کردن اشتراک
print(f"The intersection of the two lists is: {intersection}")
