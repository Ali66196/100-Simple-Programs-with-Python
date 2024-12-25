# مرتب‌سازی رشته‌ها بر اساس طول آن‌ها

# تابع برای مرتب‌سازی لیست رشته‌ها بر اساس طول آن‌ها
def sort_by_length(strings):
    return sorted(strings, key=len)

# دریافت ورودی از کاربر
strings = input("Enter strings separated by commas: ").split(", ")
sorted_strings = sort_by_length(strings)

# نمایش رشته‌ها به ترتیب طول
print(f"Strings sorted by length: {sorted_strings}")
