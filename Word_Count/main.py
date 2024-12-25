# برنامه شمارش تعداد کلمات در یک متن

# تابعی برای شمارش تعداد کلمات در یک متن
def count_words(text):
    words = text.split()  # تقسیم متن به کلمات
    return len(words)  # بازگشت تعداد کلمات

# گرفتن ورودی از کاربر برای وارد کردن متن
text = input("Enter a text: ")  # دریافت متن از کاربر

# فراخوانی تابع شمارش کلمات و نمایش نتیجه
word_count = count_words(text)  # فراخوانی تابع شمارش کلمات
print(f"The number of words in the entered text is: {word_count}")
