# برنامه تولید دنباله فیبوناچی

# تابعی برای تولید دنباله فیبوناچی
def fibonacci(n):
    fib_sequence = [0, 1]  # شروع دنباله فیبوناچی با دو عدد اول (0 و 1)
    while len(fib_sequence) < n:  # تا زمانی که تعداد اعداد کمتر از n باشد
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])  # اضافه کردن عدد بعدی به دنباله
    return fib_sequence  # بازگشت دنباله فیبوناچی

# گرفتن ورودی از کاربر برای تعداد اعداد دنباله
n = int(input("Enter the number of terms for Fibonacci sequence: "))  # دریافت تعداد اعداد از کاربر

# فراخوانی تابع و نمایش دنباله
fib_seq = fibonacci(n)  # فراخوانی تابع تولید دنباله فیبوناچی
print(f"The first {n} terms of the Fibonacci sequence are: {fib_seq}")
