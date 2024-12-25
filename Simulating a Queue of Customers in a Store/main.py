# شبیه‌سازی صف مشتریان در یک فروشگاه

from collections import deque

# تابع برای شبیه‌سازی صف مشتریان
def simulate_queue():
    queue = deque()
    
    while True:
        print("\n1. وارد کردن مشتری جدید")
        print("2. خدمات به مشتری")
        print("3. نمایش صف")
        print("4. خروج")
        choice = input("لطفاً گزینه‌ای را انتخاب کنید: ")
        
        if choice == "1":
            customer = input("نام مشتری را وارد کنید: ")
            queue.append(customer)  # افزودن مشتری به صف
            print(f"مشتری {customer} به صف اضافه شد.")
        
        elif choice == "2":
            if queue:
                served_customer = queue.popleft()  # خدمات به مشتری از ابتدای صف
                print(f"مشتری {served_customer} خدمت دریافت کرد.")
            else:
                print("هیچ مشتری در صف نیست.")
        
        elif choice == "3":
            if queue:
                print(f"مشتریان در صف: {list(queue)}")
            else:
                print("صف خالی است.")
        
        elif choice == "4":
            print("خروج از برنامه...")
            break
        else:
            print("لطفاً یک گزینه معتبر وارد کنید.")

# اجرای شبیه‌سازی
simulate_queue()
