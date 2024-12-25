# نمایش ساعت و تاریخ فعلی

from datetime import datetime

# دریافت تاریخ و ساعت فعلی
current_datetime = datetime.now()

# نمایش تاریخ و ساعت به فرمت مورد نظر
print(f"Current date and time: {current_datetime.strftime('%Y-%m-%d %H:%M:%S')}")
