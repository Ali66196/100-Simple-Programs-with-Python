# محاسبه مجموع اعداد یک فایل

# تابع برای محاسبه مجموع اعداد در فایل
def sum_numbers_in_file(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()  # خواندن تمام خطوط فایل
            total_sum = 0
            for line in lines:
                try:
                    total_sum += float(line.strip())  # تبدیل هر خط به عدد و جمع کردن آن
                except ValueError:
                    print(f"Skipping non-numeric line: {line.strip()}")
            return total_sum
    except FileNotFoundError:
        print("File not found.")
        return 0

# دریافت نام فایل از کاربر
filename = input("Enter the filename: ")

# محاسبه و نمایش مجموع اعداد در فایل
total = sum_numbers_in_file(filename)
print(f"The sum of the numbers in the file is: {total}")
