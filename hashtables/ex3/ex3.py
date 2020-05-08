def intersection(arrays):

    # set a cache
    cache = {}
    length = len(arrays)
    # store for result
    result = []
    # loop through arrays to get all numbers
    for numbers in arrays:
        # loop through numbers to get each number
        for item in numbers:
            # if each number is not in the cache
            if item not in cache:
                # add number to cache as a key and give it a value of 1
                cache[item] = 1
            # else if number is in the cache
            elif item in cache:
                cache[item] += 1
    for i in cache:
        if cache[i] == length:
            result.append(i)
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(10, 20)) + [1, 2, 3])
    arrays.append(list(range(20, 30)) + [1, 2, 3])
    arrays.append(list(range(30, 40)) + [1, 2, 3])
    # arrays.append(list(range(10, 12)) + [1, 2, 3, 4])
    print(intersection(arrays))
