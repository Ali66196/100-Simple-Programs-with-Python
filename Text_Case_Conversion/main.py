# تبدیل حروف متن به بزرگ یا کوچک

# تابعی برای تبدیل حروف به بزرگ یا کوچک
def convert_case(text, to_upper=True):
    if to_upper:
        return text.upper()  # تبدیل به حروف بزرگ
    else:
        return text.lower()  # تبدیل به حروف کوچک

# دریافت متن و نوع تبدیل از کاربر
text = input("Enter the text: ")
case_type = input("Do you want to convert to uppercase (yes/no)? ").lower()

# تبدیل متن به بزرگ یا کوچک
if case_type == "yes":
    print(f"Converted text: {convert_case(text, True)}")
else:
    print(f"Converted text: {convert_case(text, False)}")
