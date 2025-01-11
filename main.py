nums = [1,2,3,4,5]
print(nums)
new_list = [item + 1 for item in nums]
print(new_list)

name = "Salvatore"
letters = [letter for letter in name]
print(letters)

with open("file1.txt") as file:
        first_file = [int(line.strip()) for line in file.readlines()]
    
with open("file2.txt") as file:
        second_file = [int(line.strip()) for line in file.readlines()]

result = [num for num in first_file if num in second_file]

print(result)

import random

names = ["Salvo", "Federico", "Enrico", "Giovanni"]

students_scores = {student:random.randint(60,100) for student in names}

print(students_scores)