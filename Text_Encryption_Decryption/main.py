# رمزنگاری و رمزگشایی متن

from cryptography.fernet import Fernet  # وارد کردن کتابخانه برای رمزنگاری

# تولید یک کلید برای رمزنگاری
def generate_key():
    return Fernet.generate_key()

# رمزنگاری متن
def encrypt_text(key, text):
    cipher_suite = Fernet(key)
    encrypted_text = cipher_suite.encrypt(text.encode())  # رمزنگاری
    return encrypted_text

# رمزگشایی متن
def decrypt_text(key, encrypted_text):
    cipher_suite = Fernet(key)
    decrypted_text = cipher_suite.decrypt(encrypted_text).decode()  # رمزگشایی
    return decrypted_text

# دریافت کلید و متن از کاربر
key = generate_key()
text = input("Enter the text to encrypt: ")

# رمزنگاری و رمزگشایی متن
encrypted_text = encrypt_text(key, text)
print(f"Encrypted text: {encrypted_text}")
decrypted_text = decrypt_text(key, encrypted_text)
print(f"Decrypted text: {decrypted_text}")
