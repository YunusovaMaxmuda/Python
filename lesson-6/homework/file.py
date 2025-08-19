#1 Modify string with underscores
my_word = str(input('Sozni kiriting:'))
new_word = my_word.replace(" ", "_")
print(new_word) 
##2. Integer Squares Exercise
n = int(input().strip())
for i in range(n):
    print(i ** 2)

#Loop-Based Exercises

# 1. Print first 10 natural numbers using a while loop
n = 1
while n <= 10:
    print(n)
    n +=1



# 2. Print pattern
for a in range(1, 6):
    for b in range(1, a+1):
        print(b, end=" ")
    print()
# 3. Sum of numbers
n = int(input("Enter number: "))
print("Sum is:", sum(range(1, n+1)))

n  = int(input('Sonni kiriting:'))
print('Yigindi:', sum(range(1, n+1)))
# 4. Multiplication table
num = int(input("Enter number: "))
for i in range(1, 11):
    print(num * i)
son = int(input('Sonni kiriting:  '))
for n in range(1,11):
    print(son*n)
# 5. Display numbers from list
sonlar = [12, 75, 150, 180, 145, 525, 50]
for son in sonlar:
    if son > 500:
        break
    if son > 150:
        continue
    if son % 5 == 0:
        print(son)
# 6. Count digits in a number
son = 75869
print(len(str(son)))
son = 1234567890
print(len(str(son)))


# 7. Reverse number pattern
for a in range(5,0,-1):
    for b in range(a, 0, -1):
        print(b, end=" ")
    print()
# 8. Print list in reverse
list = [10,20,30,40,50]
for a in reversed(list):
    print(a)

# 9. Display numbers -10 to -1
for a in range(-10, 0):
    print(a)




# 10. Display message "Done"
for a in range(5):
  print(a)
else:
  print('Done')
# 11. Prime numbers in a range
a, b= 25, 50
print("Sonlar", a, "and",b, ":")
for son in range(a, b+1):
    if son > 1:
        for i in range(2, son):
            if son % i == 0:
                break
        else:
            print(son)


# 12. Fibonacci sequence up to 10 terms
a, b = 0, 1
print("Fibonacci:")
for _ in range(10):
    print(a, end="  ")
    a, b = b, a + b
print()

# 13. Factorial of a number
def factorial(n):
    if n  in [0,1]:
        return 1
    else:
        return n * factorial(n-1)
factorial(5)
#. Return Uncommon Elements of Lists

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
def uncommon_elements(list1, list2):
    return [x for x in list1 if x not in list2] + [x for x in list2 if x not in list1]








