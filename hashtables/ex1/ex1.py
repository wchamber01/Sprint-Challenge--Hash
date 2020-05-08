def get_indices_of_item_weights(weights, length, limit):

    # hash weights first
    # for loop to subtract
    # if answer exists add to tuple
    # limit - weight

    cache = {}

    for index, w in enumerate(weights):
        cache[w] = index
        print(cache)
    for i in weights:
        target = limit - i
        print(target)
        if target in cache:
            if cache[target] > cache[i]:
                return (cache[target])
        cache[w] = index

        for key, value in cache.items():
            if key == target:
                return (cache[w], value)

    return None


weights_3 = [4, 6, 10, 15, 16]
print('last print:', get_indices_of_item_weights(weights_3, 5, 21))
