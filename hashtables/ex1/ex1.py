def get_indices_of_item_weights(weights, length, limit):
    cache = {}
    # hash weights first for easy lookup
    # enumerate to pass index as value
    # for loop for difference
    # limit - place in the loop, look to see if that exists in the hash table and return that index

    # for index, v in enumerate(weights):
    #     for i in weights:
    #         target = limit - i
    #         if target in cache:
    #             if cache[target]
    # return None


weights_3 = [4, 6, 10, 15, 16]
print('last print:', get_indices_of_item_weights(weights_3, 5, 21))
