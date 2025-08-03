class student:
    grade = 10
    subjects = ["Math", "Science", "English"]
    subjects_scores = {
        "Math": 85,
        "Science": 90,
        "English": 88  
    }
    
    def __init__(self, name):
        self.name = name

    grade = 9
    subjects = ["Geography", "Science", "History"]
    subjects_scores = {
        "Geography": 70,
        "Science": 80,
        "History": 57  
    }
    
    def __init__(self, name):
        self.name = name


obj = student("Charlie Quinn")
obj2 = student("Sir David")
print("Objects created:", obj.name)
print("Objects created:", obj2.name)
print ("Grade:", student.grade)
print ("Subjects:", student.subjects)
print ("Subjects and Scores:")
for subject, score in student.subjects_scores.items():
    print(f"{subject}: {score}")
