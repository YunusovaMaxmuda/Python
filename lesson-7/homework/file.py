#1. is_prime(n) funksiyasi
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input("Sonni kiriting: "))
print(is_prime(n))
#2. digit_sum(k) funksiyasi
def digit_sum(k):
    return sum(int(digit) for digit in str(k))

k = int(input("Sonni kiriting: "))
print(digit_sum(k))
#3. Ikki sonning darajalari (2 ning darajalari ≤ N)
def numbers(N):
    k = 1
    while 2**k <= N:
        print(2**k, end=" ")
        k += 1

N = int(input("Sonni kiriting: "))
print(numbers(N))
