# دانلود یک صفحه وب ساده

# وارد کردن کتابخانه مورد نیاز برای دانلود محتوا
import requests

# تابعی برای دانلود صفحه وب
def download_web_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:  # اگر درخواست موفقیت‌آمیز باشد
            return response.text
        else:
            print(f"Error: Status code {response.status_code}")
    except Exception as e:
        print(f"Error downloading web page: {e}")

# دریافت URL از کاربر
url = input("Please enter the URL of the web page: ")

# دانلود و نمایش محتوای صفحه
content = download_web_page(url)
if content:
    print("Downloaded web page content:")
    print(content[:500])  # نمایش 500 کاراکتر اول محتوا
