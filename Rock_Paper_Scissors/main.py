# بازی سنگ، کاغذ، قیچی

import random  # وارد کردن کتابخانه random برای انتخاب تصادفی

# تابعی برای بازی سنگ، کاغذ، قیچی
def rock_paper_scissors():
    choices = ['rock', 'paper', 'scissors']  # گزینه‌های ممکن بازی
    user_choice = input("Enter 'rock', 'paper' or 'scissors': ").lower()  # انتخاب کاربر
    computer_choice = random.choice(choices)  # انتخاب تصادفی از سوی کامپیوتر

    print(f"Computer chose: {computer_choice}")
    
    # مقایسه انتخاب‌های کاربر و کامپیوتر
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        print("You win!")
    else:
        print("You lose!")

# فراخوانی تابع بازی
rock_paper_scissors()
