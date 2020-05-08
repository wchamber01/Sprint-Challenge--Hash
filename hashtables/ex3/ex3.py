def intersection(arrays):

    cache = {}
    new_array = []
    for item in arrays:
        # print('i:', item)
        for value in item:
            if value not in cache:
                cache[value] = 1
                print('cache:', cache)
            else:
                cache[value] += 1
        # return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(10, 20)) + [1, 2, 3])
    arrays.append(list(range(20, 30)) + [1, 2, 3])
    arrays.append(list(range(30, 40)) + [1, 2, 3])

    print(intersection(arrays))
