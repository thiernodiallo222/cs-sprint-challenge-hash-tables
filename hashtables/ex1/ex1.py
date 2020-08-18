def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    table={}
    for i in range(length):
        index = table.get(limit - weights[i])
        if index is not None:
            return i, index
        table[weights[i]] = i
    
    return None
 
 
