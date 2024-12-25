# بررسی سال کبیسه

# تابعی برای بررسی سال کبیسه
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

# دریافت سال از کاربر
year = int(input("Enter a year to check if it's a leap year: "))

# بررسی و نمایش نتیجه
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
