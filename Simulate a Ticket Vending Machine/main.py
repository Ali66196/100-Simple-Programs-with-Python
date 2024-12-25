# شبیه‌سازی ماشین نوبت‌دهی

import random  # وارد کردن کتابخانه برای تولید شماره تصادفی

# دیکشنری برای ذخیره نوبت‌ها
ticket_counter = 1

# تابع برای صدور بلیط
def issue_ticket():
    global ticket_counter
    ticket_number = ticket_counter
    ticket_counter += 1
    print(f"Your ticket number is: {ticket_number}")
    return ticket_number

# تابع برای نمایش وضعیت نوبت
def show_status(ticket_number):
    print(f"Currently serving ticket number: {ticket_number}")

# صدور بلیط و نمایش وضعیت
ticket_number = issue_ticket()
show_status(ticket_number)
