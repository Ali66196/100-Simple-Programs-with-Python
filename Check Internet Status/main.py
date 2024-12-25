# بررسی وضعیت اینترنت

import requests  # وارد کردن کتابخانه برای ارسال درخواست HTTP

# تابع برای بررسی اتصال اینترنت
def check_internet():
    try:
        # ارسال درخواست به سایت معتبر برای بررسی اتصال اینترنت
        response = requests.get("http://www.google.com", timeout=5)
        if response.status_code == 200:
            print("Internet is connected.")
        else:
            print("Internet is not connected.")
    except requests.ConnectionError:
        print("No internet connection.")

# بررسی وضعیت اینترنت
check_internet()
