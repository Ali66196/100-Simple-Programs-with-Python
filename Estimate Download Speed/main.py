# تابع برای محاسبه زمان دانلود بر اساس سرعت اینترنت و حجم فایل
def calculate_download_time():
    # دریافت حجم فایل از کاربر (بر حسب مگابایت)
    file_size_mb = float(input("Enter the file size in MB: "))
    
    # دریافت سرعت اینترنت از کاربر (بر حسب مگابیت در ثانیه)
    download_speed_mbps = float(input("Enter your internet download speed in Mbps: "))
    
    # تبدیل سرعت اینترنت از مگابیت به مگابایت
    download_speed_mb = download_speed_mbps / 8
    
    # تبدیل حجم فایل از مگابایت به بایت
    file_size_bytes = file_size_mb * 1024 * 1024
    
    # محاسبه زمان دانلود بر اساس فرمول
    download_time_seconds = file_size_bytes / (download_speed_mb * 1024 * 1024)
    
    # تبدیل زمان دانلود به دقیقه و ثانیه
    download_time_minutes = download_time_seconds / 60
    download_time_seconds_rounded = round(download_time_seconds, 2)
    
    # نمایش نتایج
    print(f"Estimated download time: {download_time_minutes:.2f} minutes ({download_time_seconds_rounded} seconds)")

# اجرای تابع محاسبه زمان دانلود
calculate_download_time()
