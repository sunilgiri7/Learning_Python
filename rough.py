def find_average(marks):
    sum_of_marks = sum(marks)
    total_subject = len(marks)
    avg_marks = sum_of_marks / total_subject
    return avg_marks


#calculate the grade and return it
def compute_grade(average_marks):
    if average_marks >= 80:
        grade = 'A'
    elif average_marks >= 60:
        grade = 'B'
    elif average_marks >= 50:
        grade = 'C'
    else:
        grade = 'fail'
        return grade
    
marks = [55, 64, 75, 80, 65]
average_marks = find_average(marks)
print("your average marks is:",average_marks)

grade = compute_grade(average_marks)
print("your grade is:",grade)