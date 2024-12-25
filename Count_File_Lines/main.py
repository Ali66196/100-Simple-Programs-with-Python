# شمارش تعداد خطوط یک فایل متنی

# تابعی برای شمارش خطوط فایل
def count_lines_in_file(file_path):
    with open(file_path, 'r') as file:  # باز کردن فایل در حالت خواندن
        lines = file.readlines()  # خواندن تمام خطوط فایل
        return len(lines)  # برگشت تعداد خطوط

# دریافت مسیر فایل از کاربر
file_path = input("Enter the path of the file: ")

# شمارش خطوط و نمایش آن
try:
    line_count = count_lines_in_file(file_path)
    print(f"The file has {line_count} lines.")
except FileNotFoundError:
    print("The file was not found.")
