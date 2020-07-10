def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    weight_store = {}
    for index, weight in enumerate(weights):
        if weight not in weight_store:
            weight_store[weight] = index
    for item in range(length):

        item_weight = weights[item]
        second_weight = limit - item_weight
        if second_weight in weight_store and weight_store[second_weight] != item:
            return(max(item, weight_store[second_weight]), min(item, weight_store[second_weight]))

    return None
