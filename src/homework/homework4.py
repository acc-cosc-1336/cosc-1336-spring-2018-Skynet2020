def sample_function(value):
    '''Return value given'''
    return value

def valid_letter_grade(letter_grade):
    x = letter_grade        
    if x == 'A' or x == 'a' or x == 'B' or x == 'b' or x == 'C' or x == 'c' or \
       x == 'D' or x == 'd' or x == 'F' or x == 'f':
        return True
    else:
        return False

def get_credit_points(letter_grade):
    '''
    Given a letter grade return the credit points associated with that grade.
    IN BLACKBOARD: SEE TABLE IN HOMEWORK 4 ASSIGNMENT.
    :param letter_grade: One letter grade
    :return: a whole number representing the credit points
    WRITE YOUR CODE AFTER THE THREE QUOTES BELOW
    '''
    credit_points = 0
    y = letter_grade
    if y == 'A' or y == 'a':
        credit_points = 4        
    elif y == 'B' or y == 'b':
        credit_points = 3        
    elif y == 'C' or y == 'c':
        credit_points = 2        
    elif y == 'D' or y == 'd':
        credit_points = 1        
    else:
        credit_points = 0        
        
    return credit_points

def get_grade_points(credit_hours, credit_points):
    '''
    Return grade points given credit hours and credit points.

    :param credit_hours: Credit hours for a class
    :param credit_points: Credit points for a class
    :return: Total grade points for a class
    '''
    grade_points = credit_hours * credit_points
    return grade_points

def get_grade_point_average(credit_hours, grade_points):
    '''
    Returns grade point average as a decimal value (float)
    :param credit_points: Total credit points for a student.
    :param grade_points: Total grade points for a student.
    :return: The grade point average for a student
    WRITE YOUR CODE AFTER THE THREE QUOTES BELOW
    '''
    GPA = grade_points / credit_hours
    return GPA
