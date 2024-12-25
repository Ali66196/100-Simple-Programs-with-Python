# برنامه جستجو در لیست

# تابعی برای جستجو در لیست
def search_in_list(numbers, target):
    if target in numbers:
        return f"{target} is found in the list."
    else:
        return f"{target} is not found in the list."

# گرفتن ورودی از کاربر برای وارد کردن لیست و عدد جستجو شده
numbers_input = input("Enter numbers separated by spaces: ")  # دریافت لیست اعداد از کاربر
numbers = [int(num) for num in numbers_input.split()]  # تبدیل ورودی به لیست اعداد
target = int(input("Enter the number you want to search for: "))  # دریافت عدد مورد نظر برای جستجو

# فراخوانی تابع و نمایش نتیجه جستجو
result = search_in_list(numbers, target)  # فراخوانی تابع جستجو
print(result)
