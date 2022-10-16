


def check_occurrences(arr):
    # check occurences, works with strings, int, tuples
    
    # only with a list
    if not type(arr) is list:
        return False

    dicc = {}
    for value in arr:
        if value in dicc:
            dicc[value] += 1
        else:
            dicc[value] = 1
    return dicc




if __name__ == '__main__':
    pass