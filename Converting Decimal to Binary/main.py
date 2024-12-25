# تبدیل اعداد اعشاری به دودویی

# تابع برای تبدیل عدد اعشاری به دودویی
def decimal_to_binary(n):
    return bin(n).replace("0b", "")  # تبدیل به دودویی و حذف "0b" پیشوند

# دریافت عدد اعشاری از کاربر
decimal_number = int(input("لطفاً یک عدد اعشاری وارد کنید: "))

# تبدیل و نمایش نتیجه
binary_number = decimal_to_binary(decimal_number)
print(f"عدد {decimal_number} به دودویی معادل {binary_number} است.")
