# List Comprehensions
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

# Dictionary comprehensions
# Exercise 1 - Create dict of word:length from sentence
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
words_dict = {word: len(word) for word in sentence.split()}
print(words_dict)

# Exercise 2 - Create dict of day: degrees F from day: degrees C
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
weather_f = {day: (temp_c * 9 / 5) + 32 for (day, temp_c) in weather_c.items()}
print(weather_f)
