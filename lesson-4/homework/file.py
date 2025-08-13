#1. Sort a Dictionary by Value
d = {"Name":"Rustam","Depertment":"Metodology","Age":35, "Salary":10000}
#2. Add a Key to a Dictionary

my_dict = {0: 10, 1: 20}
my_dict[2] = 30
print(my_dict)  
#3. Concatenate Multiple Dictionaries

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

dict = {**dic1, **dic2, **dic3}
print(dict)
#4. Generate a Dictionary with Squares (1 to n)

n = 5
squares_dict = {x: x*x for x in range(1, n+1)}
print(squares_dict)
#5. Dictionary of Squares (1 to 15)

squares_15 = {x: x*x for x in range(1, 16)}
print(squares_15)
1. Create a Set

my_set = {'a','b', 'c', 'd'}
print(my_set)
#2. Iterate Over a Set

for item in my_set:
    print(item)
  #3. Add Member(s) to a Set


my_set.add('f')


my_set.update([6, 7])
print(my_set)
#4. Remove Item(s) from a Set

my_set.remove('a')
print(my_set)
#5. Remove an Item if Present in the Set

my_set.discard('d')
print(my_set)
