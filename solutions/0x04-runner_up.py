#!/usr/bin/python3

def get_runner_up(scores):
    '''
    This function finds the runner up for the scores argument
    provided.
    '''

    # check if argument is a list or an array
    assert type(scores) == list, 'Scores should be an array'

    if len(scores) < 1:
        raise Exception('Array shouldn\'t be empty')

    # remove all duplicates from scores
    altered_scores = set(scores)
    
    # sort altered scores
    sorted_altered_scores = sorted(list(altered_scores), reverse=True)
    
    # set runner up to second largest
    runner_up = sorted_altered_scores[1]
    
    return runner_up

