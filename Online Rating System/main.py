# سیستم امتیازدهی آنلاین

class RatingSystem:
    def __init__(self):
        self.ratings = {}  # دیکشنری برای ذخیره امتیازها

    # تابع برای ثبت امتیاز
    def add_rating(self, item, rating):
        if 1 <= rating <= 5:
            self.ratings[item] = rating
            print(f"Rating {rating} for {item} has been saved.")
        else:
            print("Rating must be between 1 and 5.")

    # تابع برای نمایش امتیاز
    def get_rating(self, item):
        if item in self.ratings:
            return self.ratings[item]
        else:
            return "No rating for this item."

# ایجاد شیء از سیستم امتیازدهی
rating_system = RatingSystem()

# منوی سیستم امتیازدهی
while True:
    print("\n1. Add rating")
    print("2. Show rating")
    print("3. Exit")
    
    choice = input("Please select an option: ")
    
    if choice == "1":
        item = input("Enter the item name: ")
        rating = int(input("Enter rating (1 to 5): "))
        rating_system.add_rating(item, rating)
    elif choice == "2":
        item = input("Enter the item name: ")
        print(f"Rating for {item}: {rating_system.get_rating(item)}")
    elif choice == "3":
        print("Exiting the program...")
        break
