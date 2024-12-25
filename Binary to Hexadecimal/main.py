# تبدیل باینری به Hex

# تابع برای تبدیل باینری به Hex
def binary_to_hex(binary_string):
    hex_value = hex(int(binary_string, 2))  # تبدیل باینری به عدد صحیح و سپس به هگزادسیمال
    return hex_value

# دریافت ورودی باینری از کاربر
binary_string = input("Enter a binary number: ")

# تبدیل باینری به هگزادسیمال
hex_value = binary_to_hex(binary_string)
print(f"The hexadecimal value is: {hex_value}")
