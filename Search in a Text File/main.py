# جستجو در فایل متنی

# تابع برای جستجو در فایل
def search_in_file(filename, search_term):
    with open(filename, "r") as file:
        lines = file.readlines()  # خواندن تمام خطوط فایل
        found = False
        for line_num, line in enumerate(lines, 1):
            if search_term in line:
                print(f"Found '{search_term}' in line {line_num}: {line.strip()}")
                found = True
        if not found:
            print(f"'{search_term}' not found in the file.")

# دریافت نام فایل و عبارت جستجو از کاربر
filename = input("Please enter the filename: ")
search_term = input("Enter the term to search for: ")

# جستجو در فایل
search_in_file(filename, search_term)
