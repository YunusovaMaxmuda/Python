Exercise 1: Threaded Prime Number Checker
import threading

# Oddiy tub sonni tekshiruvchi funksiya
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Thread ishlaydigan funksiya
def check_primes(start, end, result):
    primes = []
    for num in range(start, end):
        if is_prime(num):
            primes.append(num)
    result.extend(primes)  # Natijani umumiy ro‘yxatga qo‘shamiz

if __name__ == "__main__":
    start_range = 1
    end_range = 100
    num_threads = 4  # nechta oqim ishlashini belgilaymiz

    # umumiy ro‘yxat
    result = []
    threads = []
    step = (end_range - start_range) // num_threads

    for i in range(num_threads):
        start = start_range + i * step
        end = start_range + (i + 1) * step if i < num_threads - 1 else end_range
        t = threading.Thread(target=check_primes, args=(start, end, result))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("Prime numbers:", sorted(result))

Exercise 2: Threaded File Processing
import threading
from collections import Counter

# Thread uchun funksiya
def process_lines(lines, counter):
    words = []
    for line in lines:
        words.extend(line.strip().split())
    local_count = Counter(words)
    counter.update(local_count)

if __name__ == "__main__":
    filename = "large_text.txt"
    num_threads = 4

    # Faylni o‘qish
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Faylni bo‘lib chiqamiz
    step = len(lines) // num_threads
    threads = []
    counter = Counter()

    # Threadlarni yaratish
    for i in range(num_threads):
        start = i * step
        end = (i + 1) * step if i < num_threads - 1 else len(lines)
        t = threading.Thread(target=process_lines, args=(lines[start:end], counter))
        threads.append(t)
        t.start()

    # Barcha oqimlar tugashini kutamiz
    for t in threads:
        t.join()

    # Natija chiqarish
    print("Word occurrences:")
    for word, freq in counter.most_common(10):  # eng ko‘p uchraydigan 10 ta so‘z
        print(word, ":", freq)























