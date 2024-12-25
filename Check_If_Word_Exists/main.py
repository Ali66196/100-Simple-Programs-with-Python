# بررسی اینکه یک رشته شامل یک کلمه خاص است یا نه

# تابعی برای بررسی وجود یک کلمه خاص در یک رشته
def contains_word(text, word):
    if word in text:
        return True
    else:
        return False

# دریافت رشته و کلمه از کاربر
text = input("Enter a text: ")
word = input("Enter the word to search for: ")

# بررسی وجود کلمه در رشته
if contains_word(text, word):
    print(f"The word '{word}' is found in the text.")
else:
    print(f"The word '{word}' is not found in the text.")
