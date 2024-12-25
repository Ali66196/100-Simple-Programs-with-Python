# فشرده‌سازی متن

import zlib  # وارد کردن کتابخانه برای فشرده‌سازی

# تابعی برای فشرده‌سازی متن
def compress_text(text):
    compressed = zlib.compress(text.encode())  # فشرده‌سازی متن
    return compressed

# تابعی برای بازگشایی (Decompression) متن فشرده
def decompress_text(compressed_text):
    decompressed = zlib.decompress(compressed_text).decode()  # بازگشایی متن
    return decompressed

# دریافت متن از کاربر
text = input("Enter the text to compress: ")

# فشرده‌سازی و بازگشایی متن
compressed_text = compress_text(text)
print(f"Compressed text: {compressed_text}")
decompressed_text = decompress_text(compressed_text)
print(f"Decompressed text: {decompressed_text}")
