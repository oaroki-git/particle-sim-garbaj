def sand_rule(arr, row, col, step = 1):
    active = False
    if row >= len(arr) - 1:
        return active
    if not arr[row, col]:
        return active

    #fall
    if not arr[row + 1, col]:
        arr[row, col] = False
        while row + step > arr.shape[0] - 1 or arr[row + step, col]:
            step -= 1
        arr[row + step, col] = True
        active = True
    #slide
    elif col != 0 and not arr[row + 1, col - 1]:
        arr[row, col] = False
        arr[row + 1, col - 1] = True
        active = True
    elif col != arr.shape[1] - 1 and not arr[row + 1, col + 1]:
        arr[row, col] = False
        arr[row + 1, col + 1] = True
        active = True
    return active
