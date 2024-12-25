# شمارش کلمات منحصر به فرد در یک متن

# تابع برای شمارش کلمات منحصر به فرد
def count_unique_words(text):
    words = text.split()  # تقسیم متن به کلمات
    unique_words = set(words)  # استفاده از set برای حذف تکراری‌ها
    return len(unique_words)  # برگشت تعداد کلمات منحصر به فرد

# دریافت متن از کاربر
text = input("لطفاً یک متن وارد کنید: ")

# شمارش کلمات منحصر به فرد و نمایش نتیجه
unique_word_count = count_unique_words(text)
print(f"تعداد کلمات منحصر به فرد: {unique_word_count}")
