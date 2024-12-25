# ایجاد واترمارک در عکس

from PIL import Image, ImageDraw, ImageFont  # وارد کردن کتابخانه PIL

# تابع برای اضافه کردن واترمارک به تصویر
def add_watermark(image_path, watermark_text):
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)

    # انتخاب فونت و اندازه
    font = ImageFont.load_default()
    text_width, text_height = draw.textsize(watermark_text, font)
    
    # موقعیت واترمارک در پایین راست تصویر
    position = (img.width - text_width - 10, img.height - text_height - 10)
    
    # اضافه کردن واترمارک
    draw.text(position, watermark_text, font=font, fill=(255, 255, 255, 128))  # رنگ سفید با شفافیت
    
    # نمایش تصویر
    img.show()
    img.save("watermarked_image.jpg")

# دریافت مسیر تصویر و متن واترمارک
image_path = input("Enter the path of the image: ")
watermark_text = input("Enter the watermark text: ")

# اضافه کردن واترمارک به تصویر
add_watermark(image_path, watermark_text)
