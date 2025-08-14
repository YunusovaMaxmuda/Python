#1 Age calculator

name = input("Ismingizni kiriting: ")
birth_year = int(input("Tug'ilgan yilingizni kiriting: "))
current_year = 2025
age = current_year - birth_year
print(f"{name}, sizning yoshingiz {age} da.")
#2 Extract car names
txt = 'LMaasleitbtui'
txt[1::2]
txt[0::2]
#3 Extract car names
txt = 'MsaatmiazD'
txt[::2]
txt = 'MsaatmiazD'
txt[::-2]
#4 Etract residence area
txt = "I'am John. I am from London"
words = txt.split()
if "from" in words:
    index = words.index("from")
    print("Residence area:", words[index + 1])
else:
    print("Manzil topilmadi.")
    #5 Reverse string
text = input("Matn kiriting: ")
reversed_text = text[::-1]
print("Teskarisi:", reversed_text)
#6 Count Vowels
text = input("Matn kiriting: ")
vowels = 'aeiouAEIOU'
count = sum(1 for char in text if char in vowels)
print("Unli harflar soni:", count)

#7 Find Maximum Value
numbers = list(map(int, input("Raqamlarni vergul bilan kiriting: ").split(',')))
print("Eng katta qiymat:", max(numbers))

#8 Check Palindrome
word = input("So'z kiriting: ")
if word == word[::-1]:
    print("Bu so'z palindrome.")
else:
    print("Bu so'z palindrome emas.")
word = input("So'z kiriting: ")
if word == word[::-1]:
    print("Bu so'z palindrome.")
else:
    print("Bu so'z palindrome emas.")

#9 Extract Email Domain
email = input("Email manzilini kiriting: ")
domain = email.split('@')[-1]
print("Domen:", domain)


#10 Generate Random Password
import random
import string

length = 12
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for _ in range(length))
print("Tasodifiy parol:", password)


























