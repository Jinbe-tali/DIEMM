# midterms laboratory activities
# python data structures and file handling


# part 1: lists laboratory
# task 1.1: student grade manager

students = []
grades = []

def add_student(name, grade):
    students.append(name)
    grades.append(grade)
    print(f"added {name} with grade {grade}")

def average_grade():
    return sum(grades) / len(grades) if grades else 0

def highest_grade():
    return max(grades) if grades else None

def display_students():
    print("\nstudent grades:")
    for i in range(len(students)):
        print(f"{students[i]}: {grades[i]}")

print("\ntask 1.1: student grade manager")
add_student("alice", 85)
add_student("bob", 92)
add_student("charlie", 78)

display_students()
print("\naverage grade:", average_grade())
print("highest grade:", highest_grade())


# task 1.2: list operations practice

print("\ntask 1.2: list operations practice")

numbers = [5, 2, 8, 1, 9, 3]

print("original list:", numbers)
print("sorted list:", sorted(numbers))
print("sum:", sum(numbers))
print("average:", sum(numbers) / len(numbers))
print("maximum:", max(numbers))
print("minimum:", min(numbers))
print("length:", len(numbers))


# part 2: tuples and sets laboratory
# task 2.1: coordinate system with tuples

import math

print("\ntask 2.1: coordinate system with tuples")

def distance(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

def midpoint(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

point1 = (2, 3)
point2 = (6, 7)
point3 = (1, 9)

points = (point1, point2, point3)

print("points:", points)
print("distance:", distance(point1, point2))
print("midpoint:", midpoint(point1, point2))

try:
    point1[0] = 10
except TypeError as e:
    print("tuple immutability error:", e)


# task 2.2: unique word counter with sets

print("\ntask 2.2: unique word counter with sets")

text = "Python is a programming language. Python is easy to learn. Python is powerful."

words = text.lower().replace(".", "").split()
unique_words = set(words)

print("total words:", len(words))
print("unique words:", len(unique_words))

from collections import Counter
print("most common words:", Counter(words).most_common())


# part 3: dictionaries laboratory
# task 3.1: student database

print("\ntask 3.1: student database")

students_db = {}

def add_student_db(student_id, name, grade, major):
    students_db[student_id] = {
        "name": name,
        "grade": grade,
        "major": major
    }

def get_student(student_id):
    return students_db.get(student_id, "student not found")

def update_grade(student_id, new_grade):
    if student_id in students_db:
        students_db[student_id]["grade"] = new_grade

def display_students_db():
    for sid, info in students_db.items():
        print(f"{sid}: {info}")

add_student_db(101, "alice", "a", "computer science")
add_student_db(102, "bob", "b", "it")
add_student_db(103, "charlie", "a-", "engineering")

update_grade(102, "a")
display_students_db()


# task 3.2: word frequency counter

print("\ntask 3.2: word frequency counter")

text2 = "Data structures are important. Data structures make coding efficient."

words2 = text2.lower().replace(".", "").split()
frequency = {}

for word in words2:
    frequency[word] = frequency.get(word, 0) + 1

sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

for word, count in sorted_frequency:
    print(word, ":", count)

print("most common word:", sorted_frequency[0])


# part 4: file handling laboratory
# task 4.1: student records file system

import pickle

print("\ntask 4.1: student records file system")

student_records = {
    1: {"name": "alice", "grade": "a", "major": "cs"},
    2: {"name": "bob", "grade": "b", "major": "it"}
}

def save_records(filename):
    with open(filename, "wb") as file:
        pickle.dump(student_records, file)

def load_records(filename):
    with open(filename, "rb") as file:
        return pickle.load(file)

def export_to_text(filename):
    with open(filename, "w") as file:
        for sid, info in student_records.items():
            file.write(f"{sid}: {info}\n")

save_records("students.pkl")
loaded = load_records("students.pkl")
print("loaded records:", loaded)
export_to_text("students.txt")


# task 4.2: file operations practice

print("\ntask 4.2: file operations practice")

try:
    with open("example.txt", "w") as file:
        file.write("this is a new file\n")

    with open("example.txt", "r") as file:
        print(file.read())

    with open("example.txt", "a") as file:
        file.write("this line was appended\n")

except FileNotFoundError:
    print("file not found error")
