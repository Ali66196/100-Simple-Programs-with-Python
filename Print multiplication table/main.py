# برنامه برای چاپ جدول ضرب

# تابعی برای چاپ جدول ضرب
def print_multiplication_table(number):
    print(f"Multiplication Table for {number}:")
    for i in range(1, 11):  # از 1 تا 10
        result = number * i  # ضرب عدد انتخاب شده با i
        print(f"{number} x {i} = {result}")  # چاپ نتیجه

# گرفتن ورودی از کاربر برای انتخاب عدد
num = int(input("Enter a number to display its multiplication table: "))  # دریافت عدد از کاربر

# فراخوانی تابع چاپ جدول ضرب
print_multiplication_table(num)
