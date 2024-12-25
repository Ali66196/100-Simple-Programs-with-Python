# ساخت سیستم لاگین ساده

# دیکشنری برای ذخیره کاربران و رمز عبور آنها
users_db = {"user1": "password123", "user2": "mypassword", "admin": "adminpass"}

# تابعی برای انجام لاگین
def login(username, password):
    if username in users_db and users_db[username] == password:
        return True
    else:
        return False

# دریافت نام کاربری و رمز عبور از کاربر
username = input("Enter your username: ")
password = input("Enter your password: ")

# بررسی ورود کاربر
if login(username, password):
    print("Login successful!")
else:
    print("Invalid username or password.")
