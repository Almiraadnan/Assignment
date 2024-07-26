# 1. display Alice English Score
# 2. display Bob Class
# 3. display Charlie Math Score
# 4. display Diana's avg score
# 5. display John's all subject name and score with format: Student: [Name], Score: [Subject], Score: [Score].
# 6. Add new Student and its subject, score and class in same dict i.e students
# 7. add new subject and its score in John
# """


students = {
    "Alice": {
                "Subjects": ["Math", "Science", "English"],
                "Scores": [85, 90, 78],
                "Class": 10
            },
    "Bob": {
        "Subjects": ["Math", "Science", "English"],
        "Scores": [75, 80, 88],
        "Class": 10
    },
    "Charlie": {
        "Subjects": ["Math", "Science", "English"],
        "Scores": [92, 89, 94],
        "Class": 11
    },
    "Diana": {
        "Subjects": ["Math", "Science", "English"],
        "Scores": [88, 76, 85],
        "Class": 11
    },
    "John": {
        "Subjects": ["Math", "Science", "English"],
        "Scores": [50, 60, 60],
        "Class": 11
    }
}

print(students["Alice"]["score"][2])
print(students["Bob"]["class"])
print(students["Charlie"]["score"][0])
average = students["Diana"]["score"][0]+["Diana"]["score"][1]+["Diana"]["score"][2]
print(average / 2)

print(f'student: {"John"},score:{students["John"]["Subjects"]},
      score:{students["John"]["Score"]}')
