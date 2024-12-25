# مرتب‌سازی کلمات در یک متن

# تابع برای مرتب‌سازی کلمات
def sort_words(text):
    words = text.split()  # تقسیم متن به کلمات
    words.sort()  # مرتب‌سازی کلمات
    return ' '.join(words)  # بازگشت متن مرتب‌شده

# دریافت متن از کاربر
text = input("لطفاً یک متن وارد کنید: ")

# مرتب‌سازی کلمات و نمایش نتیجه
sorted_text = sort_words(text)
print(f"متن با کلمات مرتب‌شده: {sorted_text}")
