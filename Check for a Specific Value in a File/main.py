# بررسی وجود یک مقدار خاص در فایل

# تابع برای بررسی وجود یک مقدار خاص در فایل
def check_value_in_file(filename, value):
    try:
        with open(filename, "r") as file:
            content = file.read()  # خواندن تمام محتوای فایل
            if value in content:
                print(f"The value '{value}' is present in the file.")
            else:
                print(f"The value '{value}' is not present in the file.")
    except FileNotFoundError:
        print("The file does not exist.")

# دریافت نام فایل و مقدار مورد نظر از کاربر
filename = input("Enter the filename: ")
value = input("Enter the value to search for: ")

# بررسی وجود مقدار در فایل
check_value_in_file(filename, value)
