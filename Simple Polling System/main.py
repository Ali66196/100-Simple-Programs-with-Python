# ساخت سیستم نظرسنجی ساده

class Poll:
    def __init__(self, question, options):
        self.question = question  # سوال نظرسنجی
        self.options = options  # گزینه‌ها
        self.votes = {option: 0 for option in options}  # دیکشنری برای ذخیره تعداد آرا

    # تابع برای ثبت رای
    def vote(self, option):
        if option in self.options:
            self.votes[option] += 1
            print(f"Your vote for {option} has been recorded.")
        else:
            print("Invalid option.")

    # تابع برای نمایش نتایج
    def show_results(self):
        print(f"\nPoll results: {self.question}")
        for option, count in self.votes.items():
            print(f"{option}: {count} votes")

# ایجاد شیء از سیستم نظرسنجی
poll = Poll("What kind of music do you like the most?", ["Pop", "Rock", "Classical", "Jazz"])

# منوی نظرسنجی
while True:
    print("\n1. Vote")
    print("2. Show results")
    print("3. Exit")
    
    choice = input("Please select an option: ")
    
    if choice == "1":
        print("Options:")
        for idx, option in enumerate(poll.options, start=1):
            print(f"{idx}. {option}")
        selected_option = int(input("Please enter the option number: "))
        poll.vote(poll.options[selected_option - 1])
    elif choice == "2":
        poll.show_results()
    elif choice == "3":
        print("Exiting the program...")
        break
