# تبدیل تصویر به سیاه و سفید

from PIL import Image  # وارد کردن کتابخانه PIL برای کار با تصاویر

# تابع برای تبدیل تصویر به سیاه و سفید
def convert_to_bw(image_path):
    try:
        img = Image.open(image_path)  # باز کردن تصویر
        bw_img = img.convert("L")  # تبدیل تصویر به سیاه و سفید
        bw_img.show()  # نمایش تصویر سیاه و سفید
        bw_img.save("bw_image.jpg")  # ذخیره تصویر سیاه و سفید
        print("Image has been converted to black and white and saved as 'bw_image.jpg'.")
    except Exception as e:
        print(f"Error: {e}")

# دریافت مسیر تصویر از کاربر
image_path = input("Enter the path of the image: ")

# تبدیل تصویر به سیاه و سفید
convert_to_bw(image_path)
