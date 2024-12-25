# خواندن داده‌های CSV با استفاده از کتابخانه pandas

import pandas as pd

# تابعی برای خواندن فایل CSV
def read_csv_file(file_path):
    try:
        # خواندن داده‌های CSV از فایل
        data = pd.read_csv(file_path)
        print("داده‌ها با موفقیت بارگذاری شدند:")
        print(data.head())  # نمایش چند ردیف اول داده‌ها
    except Exception as e:
        print(f"خطا در بارگذاری فایل CSV: {e}")

# نام فایل CSV را از کاربر می‌گیریم
file_path = input("لطفاً مسیر فایل CSV را وارد کنید: ")

# خواندن داده‌ها از فایل CSV
read_csv_file(file_path)
