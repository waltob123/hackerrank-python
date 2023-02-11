#!/usr/bin/python3

def check_sum_of_coords(dim1, dim2, dim3, integer_num):
    '''
    This function takes in 4 arguments. The first three arguments
    representing the dimensions of a cuboid and the second representing
    an integer.
    The functions finds all possible coordinates of the dimensions given
    and returns a list of the ones that does not sum up to be equal to the
    integer_num argument.
    '''

    # use list comprehension to get all coordinates
    resulting_list = [[i,j,k] for i in range(dim1+1)  for j in range(dim2+1) for k in range(dim3+1) if i+j+k != integer_num]

    return resulting_list

