# مدیریت فهرست خرید

# ایجاد یک لیست برای ذخیره اقلام خرید
shopping_list = []

# تابعی برای اضافه کردن یک آیتم به لیست خرید
def add_item(item):
    shopping_list.append(item)

# تابعی برای نمایش لیست خرید
def show_list():
    if not shopping_list:
        print("Shopping list is empty.")
    else:
        print("Shopping List:")
        for item in shopping_list:
            print(f"- {item}")

# منوی ساده برای مدیریت فهرست خرید
while True:
    print("\nShopping List Menu:")
    print("1. Add Item")
    print("2. Show List")
    print("3. Exit")

    choice = input("Enter your choice: ")
    
    if choice == '1':
        item = input("Enter the item to add: ")
        add_item(item)
    elif choice == '2':
        show_list()
    elif choice == '3':
        break
    else:
        print("Invalid choice.")
