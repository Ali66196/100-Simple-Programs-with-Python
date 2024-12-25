# پیدا کردن کلمه با بیشترین تعداد تکرار در یک متن

from collections import Counter

# تابع برای پیدا کردن کلمه با بیشترین تعداد تکرار
def most_frequent_word(text):
    words = text.split()  # تقسیم متن به کلمات
    word_counts = Counter(words)  # شمارش تعداد تکرار هر کلمه
    most_common = word_counts.most_common(1)  # پیدا کردن کلمه پر تکرار
    return most_common[0]  # برگشت کلمه و تعداد آن

# دریافت متن از کاربر
text = input("لطفاً یک متن وارد کنید: ")

# پیدا کردن کلمه پر تکرار و نمایش نتیجه
word, count = most_frequent_word(text)
print(f"کلمه با بیشترین تکرار: {word} (تعداد تکرار: {count})")
