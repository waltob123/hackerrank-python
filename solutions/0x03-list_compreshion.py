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

    # setting resulting array
    resulting_list = []

    # setting a temporary array to hold each coordinate
    coordinate = []

    # looping through all dimensions to get coordinates
    for i in range(dim1+1):
        for j in range(dim2+1):
            for k in range(dim3+1):
                if i + j + k != integer_num:
                    coordinate.append(i)
                    coordinate.append(j)
                    coordinate.append(k)
                    resulting_list.append(coordinate)
                    coordinate = []
                else:
                    continue
    return resulting_list
