# تولید شعر با کلمات تصادفی

import random

# لیستی از کلمات برای ساخت شعر
words = ["sky", "love", "moon", "shine", "stars", "dream", "light", "beauty", "heart"]

# تابعی برای تولید شعر تصادفی
def generate_poem():
    poem = random.sample(words, 4)  # انتخاب 4 کلمه تصادفی از لیست
    return " ".join(poem)  # ساخت شعر از کلمات

# تولید و نمایش شعر
print("Generated Poem:")
print(generate_poem())
