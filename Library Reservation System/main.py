# ساخت سیستم رزرو کتابخانه

class Library:
    def __init__(self):
        # دیکشنری برای ذخیره کتاب‌ها و وضعیت رزرو آن‌ها
        self.books = {
            "Book 1": False,
            "Book 2": False,
            "Book 3": False,
            "Book 4": False,
        }

    # تابع برای رزرو کتاب
    def reserve_book(self, book_name):
        if book_name in self.books:
            if self.books[book_name]:
                print(f"'{book_name}' has already been reserved.")
            else:
                self.books[book_name] = True
                print(f"'{book_name}' has been reserved for you.")
        else:
            print(f"'{book_name}' is not available in the library.")

    # تابع برای نمایش وضعیت کتاب‌ها
    def show_books(self):
        print("Books in Library:")
        for book, reserved in self.books.items():
            status = "Reserved" if reserved else "Available"
            print(f"{book}: {status}")


# ایجاد شیء کتابخانه و استفاده از آن
library = Library()
library.show_books()

# رزرو کتاب
book_name = input("Enter the name of the book you want to reserve: ")
library.reserve_book(book_name)

# نمایش وضعیت کتاب‌ها پس از رزرو
library.show_books()
