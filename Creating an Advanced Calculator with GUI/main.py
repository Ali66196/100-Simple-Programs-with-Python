# ایجاد ماشین حساب پیشرفته با استفاده از Tkinter

import tkinter as tk

# تابع برای انجام محاسبات
def calculate():
    try:
        result = eval(entry.get())  # محاسبه ورودی کاربر
        result_label.config(text=f"Result: {result}")
    except Exception as e:
        result_label.config(text="Error")

# ایجاد پنجره اصلی
window = tk.Tk()
window.title("Advanced Calculator")

# ورودی برای دریافت عبارت ریاضی
entry = tk.Entry(window, width=30)
entry.grid(row=0, column=0, columnspan=4)

# دکمه‌های ماشین حساب
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

# افزودن دکمه‌ها به پنجره
for (text, row, col) in buttons:
    tk.Button(window, text=text, width=10, height=2, command=lambda t=text: entry.insert(tk.END, t) if t != "=" else calculate()).grid(row=row, column=col)

# نمایش نتیجه
result_label = tk.Label(window, text="Result: ", width=30)
result_label.grid(row=5, column=0, columnspan=4)

# اجرای رابط کاربری
window.mainloop()
