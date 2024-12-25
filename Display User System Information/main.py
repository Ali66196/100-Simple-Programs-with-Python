# نمایش اطلاعات سیستم کاربر

import platform  # وارد کردن کتابخانه برای دریافت اطلاعات سیستم

# تابع برای نمایش اطلاعات سیستم
def display_system_info():
    system_info = platform.uname()  # دریافت اطلاعات سیستم
    print("System Information:")
    print(f"System: {system_info.system}")
    print(f"Node Name: {system_info.node}")
    print(f"Release: {system_info.release}")
    print(f"Version: {system_info.version}")
    print(f"Machine: {system_info.machine}")
    print(f"Processor: {system_info.processor}")

# نمایش اطلاعات سیستم
display_system_info()
