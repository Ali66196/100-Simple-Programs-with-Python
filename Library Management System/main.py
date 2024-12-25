# برنامه مدیریت کتابخانه

class Library:
    def __init__(self):
        self.books = {}
    
    # تابع برای اضافه کردن کتاب جدید
    def add_book(self, book_name, author):
        self.books[book_name] = author
    
    # تابع برای نمایش لیست کتاب‌ها
    def show_books(self):
        if self.books:
            print("\nBooks in the Library:")
            for book, author in self.books.items():
                print(f"Book: {book}, Author: {author}")
        else:
            print("No books in the library.")
    
    # تابع برای حذف یک کتاب
    def remove_book(self, book_name):
        if book_name in self.books:
            del self.books[book_name]
            print(f"The book '{book_name}' has been removed.")
        else:
            print(f"The book '{book_name}' does not exist.")

# ایجاد یک شیء از کتابخانه
library = Library()

# تعامل با کاربر برای مدیریت کتابخانه
while True:
    print("\n1. Add Book")
    print("2. Show Books")
    print("3. Remove Book")
    print("4. Exit")
    
    choice = input("Choose an option: ")
    
    if choice == "1":
        book_name = input("Enter book name: ")
        author = input("Enter author name: ")
        library.add_book(book_name, author)
    elif choice == "2":
        library.show_books()
    elif choice == "3":
        book_name = input("Enter book name to remove: ")
        library.remove_book(book_name)
    elif choice == "4":
        print("Exiting the program...")
        break
    else:
        print("Invalid option, please try again.")
