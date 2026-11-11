# AI-based Student Performance Prediction
print("STUDENT PERFORMANCE PREDICTION")
print("--------------------------------")

student_name = input("Enter student name: ")
marks = float(input("Enter student marks: "))

if marks >= 40 and marks <= 100:
    print("Student Name:", student_name)
    print("Marks:", marks)
    print("Prediction: PASS")

elif marks >= 0 and marks < 40:
    print("Student Name:", student_name)
    print("Marks:", marks)
    print("Prediction: FAIL")

else:
    print("Invalid marks! Enter marks between 0 and 100.")
