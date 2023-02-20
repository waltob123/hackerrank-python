#/usr/bin/python3

def convert_to_tuple():
    '''
    This function takes an input from the user and converts it
    into a tuple and returns the hash value of the tuple
    '''

    # get user input, split it and convert each value to a string
    user_input = map(str, input('Enter your values here: ').split())

    # convert user input to tuple
    tuple_value = tuple(user_input)

    # get the hash value for the tuple
    hash_value = hash(tuple_value)

    return hash_value

