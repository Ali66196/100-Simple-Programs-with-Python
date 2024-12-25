# تولید لیست از اعداد اول

# تابع برای بررسی اینکه آیا یک عدد اول است یا خیر
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# تابع برای تولید لیست اعداد اول
def generate_primes(limit):
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes

# دریافت حد از کاربر و نمایش اعداد اول
limit = int(input("Enter the limit to generate prime numbers: "))
primes = generate_primes(limit)
print(f"Prime numbers up to {limit}: {primes}")
