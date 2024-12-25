# بازی حدس عدد

import random  # وارد کردن کتابخانه random برای تولید عدد تصادفی

# تابعی برای بازی حدس عدد
def guess_the_number():
    # تولید یک عدد تصادفی بین 1 و 100
    number_to_guess = random.randint(1, 100)
    attempts = 0  # شمارش تعداد تلاش‌ها

    print("Welcome to the Guess the Number game!")
    print("I have selected a number between 1 and 100. Try to guess it.")

    # حلقه تا زمانی که عدد حدس زده نشده باشد
    while True:
        guess = int(input("Enter your guess: "))  # گرفتن حدس از کاربر
        attempts += 1  # افزایش تعداد تلاش‌ها

        # بررسی حدس کاربر
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number in {attempts} attempts.")
            break  # پایان بازی پس از درست حدس زدن عدد

# فراخوانی تابع بازی
guess_the_number()
