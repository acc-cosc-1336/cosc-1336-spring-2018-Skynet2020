def sample_function(value):
    '''Return value given'''
    return value
##-------------------------------------------------------



def valid_letter_grade(letter_grade):
    x = letter_grade        
    if x == 'A' or x == 'a':
        letter_grade = x
    elif x == 'B' or x == 'b':
        letter_grade = x
    elif x == 'C' or x == 'c':
        letter_grade = x
    elif x == 'D' or x == 'd':
        letter_grade = x
    elif x == 'F' or x == 'f':
        letter_grade = x
##    else:
##        print('Incorrect grade')
##        x = letter_grade
    return letter_grade
##------------------------------------------------------


def get_credit_points(letter_grade):
    '''
    Given a letter grade return the credit points associated with that grade.
    IN BLACKBOARD: SEE TABLE IN HOMEWORK 4 ASSIGNMENT.
    :param letter_grade: One letter grade
    :return: a whole number representing the credit points
    WRITE YOUR CODE AFTER THE THREE QUOTES BELOW
    '''
    y = valid_letter_grade(letter_grade)
    credit_points = 0
    if y == 'A' or y == 'a':
        credit_points = 4        
    elif y == 'B' or y == 'b':
        credit_points = 3        
    elif y == 'C' or y == 'c':
        credit_points = 2        
    elif y == 'D' or y == 'd':
        credit_points = 1        
    elif y == 'F' or y == 'f':
        credit_points = 0        
    else:
        print('Seems that you entered an incorect letter grade')
        x = input('Enter a valid letter grade here: ')
        print(credit_points)
        
    return credit_points
##-------------------------------------------------------


def get_grade_points(credit_hours, credit_points):
    '''
    Return grade points given credit hours and credit points.

    :param credit_hours: Credit hours for a class
    :param credit_points: Credit points for a class
    :return: Total grade points for a class
    '''
    grade_points = credit_hours * credit_points
    print('Grade point for this class is: ', format(grade_points, '.2f'))
    return grade_points


##--------------------------------------------------------


##grade_points = get_grade_points(credit_hours, credit_points)

def get_grade_point_average(credit_hours, grade_points):
    '''
    Returns grade point average as a decimal value (float)
    :param credit_points: Total credit points for a student.
    :param grade_points: Total grade points for a student.
    :return: The grade point average for a student
    WRITE YOUR CODE AFTER THE THREE QUOTES BELOW
    '''
    GPA = grade_points / credit_hours
    print('GPA is: ', format(GPA, '.2f'))
    return GPA

##get_grade_point_average(credit_hours, grade_points)
