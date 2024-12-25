# خواندن و نوشتن فایل متنی

# نوشتن متن به یک فایل
def write_to_file(file_path, text):
    with open(file_path, 'w') as file:
        file.write(text)

# خواندن متن از یک فایل
def read_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# دریافت نام فایل و متن از کاربر
file_path = input("Enter the file path: ")
text_to_write = input("Enter the text you want to write to the file: ")

# نوشتن به فایل
write_to_file(file_path, text_to_write)

# خواندن از فایل و نمایش محتوا
file_content = read_from_file(file_path)
print(f"The content of the file is:\n{file_content}")
