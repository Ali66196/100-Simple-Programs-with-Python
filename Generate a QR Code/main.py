# تولید یک QR Code

import qrcode  # وارد کردن کتابخانه QR code

# تابع برای تولید QR Code
def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill="black", back_color="white")
    img.show()  # نمایش QR Code به صورت تصویر

# دریافت ورودی از کاربر برای تولید QR Code
data = input("Enter the data for QR code: ")

# تولید QR Code
generate_qr_code(data)
