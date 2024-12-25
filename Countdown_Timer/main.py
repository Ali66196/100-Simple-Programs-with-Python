# تایمر شمارش معکوس

import time

# تابعی برای شمارش معکوس
def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)  # تبدیل ثانیه‌ها به دقیقه و ثانیه
        timeformat = f'{mins:02}:{secs:02}'  # فرمت زمان
        print(timeformat, end='\r')  # نمایش زمان به صورت شمارش معکوس
        time.sleep(1)  # تاخیر یک ثانیه‌ای
        seconds -= 1
    print("Time's up!")

# دریافت زمان از کاربر
seconds = int(input("Enter the countdown time in seconds: "))

# فراخوانی تابع تایمر شمارش معکوس
countdown_timer(seconds)
