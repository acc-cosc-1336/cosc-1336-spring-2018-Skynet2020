#write the import statements to bring in homework 4 functions
#valid_letter_grade, get_credit_points, get_grade_points, and get_grade_point_average
from src.homework.homework4 import valid_letter_grade
from src.homework.homework4 import get_credit_points
from src.homework.homework4 import get_grade_points
from src.homework.homework4 import get_grade_point_average
'''
Use the functions from homework4 to...
Write code to prompt the user for number of students and grades.
Create a nested loop to collect letter grades and credit hours for each student.
Vaidate the letter grade is in accepted range if not prompt user for letter again.
From the letter grade, get the credit points for that class.
Calculate grade points (How? Research GPA calculation).
Sum grade points and credit hours for each student.
Calculate GPA for each student.
Display Student 1(etc) GPA is 3.77. Format the GPA to two values.
'''

#WRITE YOUR CODE IN THE MAIN FUNCTION BELOW 
def main():
    how_many_students = int(input('Enter the number of students here: '))    
    how_many_classes = int(input('Enter the number of classes here: '))
    print()
    
    for i in range(1, how_many_students+1):        
        total_grade_points = 0
 +      total_credit_hours = 0  
        print('For student', str(i))
        for n in range(1, how_many_classes+1):
            grade = input('Enter a letter grade for class ' + \
                           str(n) +\
                            ': ') 
            valid = valid_letter_grade(grade)
 +            while not valid:
 +                grade = input('Enter a letter grade for class ' + \
 +                           str(n) +\
 +                            ': ')            
 +                valid = valid_letter_grade(grade)
 +                
 +            credit_points = get_credit_points(grade)
            credit_hours = int(input('Enter credit hours for class ' +\
                                 str(n) +\
                                  ' here: '))
           
            grade_points = get_grade_points(credit_hours, credit_points)
 +            total_credit_hours += credit_hours
 +            total_grade_points += grade_points
        
        GPA = get_grade_point_average(total_credit_hours, total_grade_points)
 +        print("Student", i, "GPA is", format(GPA, ".2f"))
        print()
         
#CALL THE MAIN FUNCTION

main()
