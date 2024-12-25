# محاسبه روزهای باقی‌مانده تا یک تاریخ مشخص

from datetime import datetime

# دریافت تاریخ هدف از کاربر
target_date_input = input("Enter the target date (YYYY-MM-DD): ")
target_date = datetime.strptime(target_date_input, "%Y-%m-%d")  # تبدیل ورودی به شیء تاریخ

# محاسبه تعداد روزهای باقی‌مانده
today = datetime.today()
days_left = (target_date - today).days

# نمایش نتیجه
if days_left > 0:
    print(f"{days_left} days left until {target_date_input}.")
else:
    print(f"The target date {target_date_input} has passed.")
