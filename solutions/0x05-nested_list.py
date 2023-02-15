#!/usr/bin/python3

def get_stds_sec_least_score(students):
    '''
    This function takes in array of students name and score inside
    an array and prints out all student who got the second lowest
    grade in alphabetically order.
    '''

    # check if argument is an array
    assert type(students) == list, 'Function takes in an array as an argument'
    
    # check if all array elements is an array
    try:
        for i in range(len(students)):
            assert type(students[i]) == list, 'Array elements should be an array'
            assert len(students[i]) == 2, 'Length of array elements should be 2'
    except AssertionError:
        return 'Array elements should be an array and of length 2'

    # get all scores
    scores = []
    for student in students:
        scores.append(student[1])

    # get second lowest score
    second_lowest = sorted(list(set(scores)))[1]

    # students with second lowest score
    stds_sec_lowest_score = []

    # loop through students to add to stds_sec_lowest_score array
    for student in students:
        # check if student score is equal to second_lowest
        if student[1] == second_lowest:
            stds_sec_lowest_score.append(student[0])


    return f'Sorted list {sorted(stds_sec_lowest_score)}'

