# ساخت بازی پازل ریاضی

import random  # وارد کردن کتابخانه random برای تولید اعداد تصادفی

# تابعی برای تولید یک سوال جمع ساده
def math_puzzle():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    correct_answer = num1 + num2  # جمع دو عدد
    user_answer = int(input(f"What is {num1} + {num2}? "))  # دریافت جواب از کاربر
    
    if user_answer == correct_answer:
        print("Correct! Well done.")
    else:
        print(f"Wrong! The correct answer is {correct_answer}.")

# فراخوانی تابع پازل
math_puzzle()
