#!/usr/bin/python3

def find_the_percentage(students, student_name, /):
    '''
    This function takes in two positional arguments - a students dictionary containing
    the name of a student as a key and an array of marks as a value and the second argument
    is the name of student to calculate their marks percentage.
    '''

    # check if students is a dictionary and is not empty and student_name is a string.
    assert type(students) == dict, 'Argument at position 0 should be of type dict'
    assert type(student_name) == str, 'Argument at position 1 should be of type str'

    if len(students) < 1 or len(student_name) < 1:
        raise Exception('Both arguments should not be of length 0')

    # set a variable to store student marks
    student_marks = students.get(student_name, 'Sorry, student does not exist')

    # calculate average mark of student and store it
    if type(student_marks) == list:
        try:
            average_mark = sum(student_marks) / len(student_marks)
        except TypeError:
            return 'Argument at position 0 value should contain items only of type int or float'
        except ZeroDivisionError:
            return '0.00'
    else:
        print(student_marks)
        return 'Argument at position 0 values should be of type list'

    return '{mark:.2f}'.format(mark=average_mark)

