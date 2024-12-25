# خواندن اطلاعات تصویر (مانند فرمت و اندازه)

from PIL import Image  # وارد کردن کتابخانه PIL برای کار با تصاویر

# تابع برای خواندن اطلاعات تصویر
def read_image_info(image_path):
    try:
        img = Image.open(image_path)  # باز کردن تصویر
        img_format = img.format  # فرمت تصویر
        img_size = img.size  # اندازه تصویر (عرض و ارتفاع)
        img_mode = img.mode  # حالت رنگی تصویر (مانند RGB)
        print(f"Image Format: {img_format}")
        print(f"Image Size: {img_size[0]}x{img_size[1]}")
        print(f"Image Mode: {img_mode}")
    except Exception as e:
        print(f"Error: {e}")

# دریافت مسیر تصویر از کاربر
image_path = input("Enter the path of the image: ")

# خواندن اطلاعات تصویر
read_image_info(image_path)
