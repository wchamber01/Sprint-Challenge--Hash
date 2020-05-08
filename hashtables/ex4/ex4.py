def has_negatives(a):
    # initialize a cache to hold all numbers
    cache = {}
    # initialize a list for results
    results = list()

    # loop over each number in the list
    for num in a:

        # if the number has a corresponding number in the cache
        if cache.get(abs(num)):

            # validate - if sums == 0
            if (num + cache.get(abs(num))) == 0:

                # if yes, append to results
                results.append(abs(num))
        else:
            # if no value is found, pass num as new key along with it's value

            cache[abs(num)] = num
            # print('cache:', cache)

    return results


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
