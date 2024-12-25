# شمارش تعداد کاراکترهای خاص در متن

# تابع برای شمارش کاراکترهای خاص
def count_characters(text, char):
    return text.count(char)  # شمارش تعداد وقوع کاراکتر در متن

# دریافت ورودی از کاربر
text = input("Please enter some text: ")
char = input("Which character would you like to count? ")

# شمارش و نمایش نتیجه
count = count_characters(text, char)
print(f"The number of occurrences of '{char}' in the text is: {count}")
