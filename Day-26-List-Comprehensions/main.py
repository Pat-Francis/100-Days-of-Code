# Exercise 1 - Square the numbers
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [number ** 2 for number in numbers]
print(squared_numbers)

# Exercise 2 - Filter even numbers
filtered_nums = [number for number in numbers if number % 2 == 0]
print(filtered_nums)

# Exercise 3 - Data overlap - Create list of integers in file 1.txt and file2.txt
with open("file1.txt") as f1:
    file1 = f1.read().splitlines()
with open("file2.txt") as f2:
    file2 = f2.read().splitlines()

overlap = [int(number) for number in file1 if number in file2]
print(overlap)