#1 Create and Access List Elements

fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
print(fruits[2]) 
#2 Concatenate Two Lists

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
list1
#3 Extract Elements from a List

numbers = [10, 20, 30, 40, 50]
birinchi = numbers[0]
ikkinchi = numbers[len(numbers) // 2]
uchinchi = numbers[-1]
new_list = [birinchi, ikkinchi, uchinchi]
print(new_list) 
#4 Convert List to Tuple

names = ['Nigora', 'Maxmuda', 'Madina', 'Muslima', 'Xadicha']
names_tuple = tuple(names)
print(names_tuple)
#5 Check Element in a List

cities = ['New York', 'London', 'Paris', 'Tokyo']
print('Paris' in cities) 
#5 Check Element in a List

cities = ['New York', 'London', 'Paris', 'Tokyo']
print('Tashkent' in cities)
#6 Duplicate a List Without Using Loops

numbers = [1, 2, 3]
duplicated = numbers * 3
print(duplicated)  
#7 Swap First and Last Elements of a List

numbers = [1, 2, 3, 4, 5]
numbers[0], numbers[-1] = numbers[-1], numbers[0]
print(numbers)  
list3 = [1,2,3,4,5]
list3.reverse()
list3
#8 Slice a Tuple

num_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(num_tuple[5:9])
#9 Count Occurrences in a List

colors = ['banan', 'apple', 'grape', 'banan', 'peach', 'banan']
banan_count = colors.count('banan')
print(banan_count)  
#10. Find the Index of an Element in a Tuple

animals = ('cat', 'dog', 'lion', 'tiger')
index = animals.index('lion')
print(index)
numbers = (1, 2, 3, 4)
index = numbers.index(3)
print(index) 
# 11. Merge Two Tuples

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
tuple = tuple1 + tuple2
print(tuple) 
# 12. Find the Length of a List and Tuple

my_list = [10, 20, 30]
my_tuple = (40, 50, 60, 70)
print(len(my_list))  
print(len(my_tuple))
#13. Convert Tuple to List

my_tuple = ('a', 'b', 'c', 'd')
my_list = list(my_tuple)

print(my_list)
#14. Find Maximum and Minimum in a Tuple

numbers = (7, 2, 9, 4, 1)
print(max(numbers))  
print(min(numbers))  
#15. Reverse a Tuple

words = ('a', 'b', 'c', 'd')
reversed_words = words[::-1]
print(reversed_words) 
