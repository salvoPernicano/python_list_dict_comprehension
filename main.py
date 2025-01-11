import pandas
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

passed_students = {student:value for (student,value) in students_scores.items() if value > 70}

print("Students and Scores:", students_scores)
print("Passed Students:", passed_students)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word:len(word) for word in sentence.split()}
print(result)

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {day:(value * 9/5) + 32 for (day,value) in weather_c.items()}

print(weather_f)


student_dict = {
        "student" : ["Angela", "Giulia", "Sara"],
        "scores" : [99,94,87]
}
indirizzi = ["Mosca", "Roma", "Catania"]
student_data_frame = pandas.DataFrame(student_dict)

student_data_frame["city"] = indirizzi

for(index,row) in student_data_frame.iterrows():
        print(row)

nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")

print(nato_df)

alphabet_dict = nato_df.set_index("letter")["code"].to_dict()
print(alphabet_dict)
user_input = input("What s the word to code?").upper()
user_input_list = [alphabet_dict[char] for char in user_input]
print(user_input_list)
