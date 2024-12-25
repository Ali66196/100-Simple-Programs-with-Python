# تبدیل متن به فرمت JSON

import json  # وارد کردن کتابخانه json

# تابعی برای تبدیل یک دیکشنری به فرمت JSON
def text_to_json(text):
    text_dict = {"text": text}
    json_text = json.dumps(text_dict, ensure_ascii=False, indent=4)  # تبدیل به JSON
    return json_text

# دریافت متن از کاربر
text = input("Enter the text to convert to JSON: ")

# تبدیل متن به JSON و نمایش آن
json_output = text_to_json(text)
print("Converted JSON:")
print(json_output)
