# AI-based Student Performance Analysis
student_marks = 85
passing_marks = 40
maximum_marks = 100

# Arithmetic Operators
bonus_marks = 5
total_marks = student_marks + bonus_marks

print("STUDENT PERFORMANCE ANALYSIS")
print("--------------------------------")
print("Original Marks:", student_marks)
print("Bonus Marks:", bonus_marks)
print("Total Marks:", total_marks)

# Comparison Operators
print("Passed:", total_marks >= passing_marks)
print("Full Marks:", total_marks == maximum_marks)

# Logical Operators
if total_marks >= passing_marks and total_marks <= maximum_marks:
    print("Prediction: PASS")
else:
    print("Prediction: FAIL")

# Additional Arithmetic Operators
print("Marks after deduction:", total_marks - 5)
print("Double Marks:", total_marks * 2)
print("Half Marks:", total_marks / 2)
