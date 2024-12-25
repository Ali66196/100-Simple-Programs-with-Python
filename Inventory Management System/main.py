# سیستم مدیریت داده‌های انبار

class Inventory:
    def __init__(self):
        self.items = {}  # دیکشنری برای ذخیره کالاها

    # تابع برای افزودن کالا
    def add_item(self, name, quantity):
        if name in self.items:
            self.items[name] += quantity
        else:
            self.items[name] = quantity
        print(f"{quantity} units of {name} added to inventory.")

    # تابع برای حذف کالا
    def remove_item(self, name, quantity):
        if name in self.items and self.items[name] >= quantity:
            self.items[name] -= quantity
            print(f"{quantity} units of {name} removed from inventory.")
        else:
            print("Item is not available or insufficient quantity.")

    # تابع برای نمایش موجودی انبار
    def show_inventory(self):
        if self.items:
            print("\nInventory:")
            for item, quantity in self.items.items():
                print(f"{item}: {quantity} units")
        else:
            print("Inventory is empty.")

# ایجاد شیء از سیستم انبار
inventory = Inventory()

# منوی سیستم مدیریت انبار
while True:
    print("\n1. Add item")
    print("2. Remove item")
    print("3. Show inventory")
    print("4. Exit")
    
    choice = input("Please select an option: ")
    
    if choice == "1":
        item_name = input("Enter item name: ")
        quantity = int(input("Enter item quantity: "))
        inventory.add_item(item_name, quantity)
    elif choice == "2":
        item_name = input("Enter item name: ")
        quantity = int(input("Enter item quantity: "))
        inventory.remove_item(item_name, quantity)
    elif choice == "3":
        inventory.show_inventory()
    elif choice == "4":
        print("Exiting the program...")
        break
