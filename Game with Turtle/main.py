# طراحی بازی ساده با Turtle

import turtle  # وارد کردن کتابخانه turtle برای طراحی بازی

# تنظیمات صفحه و قلم
screen = turtle.Screen()
screen.title("Simple Turtle Game")
screen.bgcolor("lightblue")

player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.penup()
player.goto(0, -200)

# حرکت دادن لاک‌پشت به چپ و راست
def move_left():
    x = player.xcor() - 20
    player.setx(x)

def move_right():
    x = player.xcor() + 20
    player.setx(x)

# کنترل‌های صفحه کلید
screen.listen()
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

# اجرای بازی تا زمانی که پنجره بسته نشود
screen.mainloop()
