# شمارش تعداد جملات در متن

import re  # وارد کردن کتابخانه برای جستجو با الگو

# تابعی برای شمارش تعداد جملات
def count_sentences(text):
    sentences = re.split(r'[.!?]', text)  # تقسیم متن بر اساس نقطه، علامت سوال یا تعجب
    sentences = [s for s in sentences if s]  # حذف مقادیر خالی
    return len(sentences)

# دریافت متن از کاربر
text = input("Enter a text to count sentences: ")

# شمارش تعداد جملات
num_sentences = count_sentences(text)
print(f"Number of sentences: {num_sentences}")
