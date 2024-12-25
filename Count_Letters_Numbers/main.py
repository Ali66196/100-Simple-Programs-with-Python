# شمارش حروف و اعداد در یک متن

# تابعی برای شمارش حروف و اعداد
def count_characters_and_numbers(text):
    letters = 0
    digits = 0
    for char in text:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            digits += 1
    return letters, digits

# دریافت متن از کاربر
text = input("Enter the text to count letters and digits: ")

# شمارش حروف و اعداد
letters, digits = count_characters_and_numbers(text)
print(f"Letters: {letters}, Digits: {digits}")
