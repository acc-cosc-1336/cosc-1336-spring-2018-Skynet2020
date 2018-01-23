time_passed = 3800
def get_hours_since_midnight(time_passed):
    '''
    Type the code to calculate total hours given n(number) of seconds
    For example, given 3800 seconds the total hours is 1
    '''
    return time_passed // 3600
hours = get_hours_since_midnight(time_passed)


'''
IF YOU ARE OK WITH A GRADE OF 70 FOR THIS ASSIGNMENT STOP HERE.
'''

def get_minutes(time_passed):
    '''
    Type the code to calculate total minutes less whole hour given n(number) of seconds
    For example, given 3800 seconds the total minutes is 3
    '''

    return int((time_passed / 60) % 60)
minutes = get_minutes(time_passed)


def get_seconds(time_passed):
    '''
    Type the code to calculate total minutes less whole hour given n(number) of seconds
    For example, given 3800 seconds the total minutes is 20
    '''

    return time_passed % 60
seconds = get_seconds(time_passed)

print('Time passed since midnight: ', hours, ': 0' + str(minutes), ':', seconds)

## 1. I created a variable "time_passed" and assigned it a value of  3800.
## 2. I developed the functions (get_hours_since_midnight, get_minutes & get_seconds),
## making them count hours, minutes and seconds basing on integer division
## and remainder division operators.
## 3. The "print" function outputs an informational string first,
## telling the user what is going to be displayed, and after that consequentally
## displays the result of previous calculations.
## 4. Also I added "str" function to the minutes inside the "print" function's arguments in order to
## display the final result in time format. I'm sure there's a way to do that properly without changing
## the type of the argument, but I don't know it yet.
