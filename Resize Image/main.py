# تغییر اندازه تصویر

from PIL import Image  # وارد کردن کتابخانه PIL برای کار با تصاویر

# تابع برای تغییر اندازه تصویر
def resize_image(image_path, new_width, new_height):
    try:
        img = Image.open(image_path)  # باز کردن تصویر
        resized_img = img.resize((new_width, new_height))  # تغییر اندازه تصویر
        resized_img.show()  # نمایش تصویر تغییر اندازه داده شده
        resized_img.save("resized_image.jpg")  # ذخیره تصویر با اندازه جدید
        print(f"Image has been resized to {new_width}x{new_height} and saved as 'resized_image.jpg'.")
    except Exception as e:
        print(f"Error: {e}")

# دریافت مسیر تصویر و ابعاد جدید از کاربر
image_path = input("Enter the path of the image: ")
new_width = int(input("Enter the new width: "))
new_height = int(input("Enter the new height: "))

# تغییر اندازه تصویر
resize_image(image_path, new_width, new_height)
