year = int(input("Yilni kiriting: "))
if (year % 4 == 0):
    if (year % 100 == 0):
        if (year % 400 == 0):
            print('Bu kabisa yili')
        else:
            print('Bu oddiy yil')

    else:
        print('Bu kabisa yili')

else:
    print('Bu oddiy yil')
def is_leap(year):

    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")

    return (year % 4 == 0 and year % 100 !=n = int(input().strip())

if n % 2 != 0:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")

a, b = map(int, input().split())

if a % 2 != 0:
    a += 1  

if a <= b:
    print(list(range(a, b + 1, 2)))
else:
    print([])
a, b = map(int, input().split())

c = list(range(a + (a % 2), b + 1, 2))
print(c)















