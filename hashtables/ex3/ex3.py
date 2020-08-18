 
def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # dict_arrays={}
    result=[]
    # for i in range (len(arrays)):
    #     dict_arrays[i]=arrays[i]

    first = arrays[0]
    # for j in range (len(first)):
    #     single[j]=first[j]

    for i in range(len(arrays)):
        if i < len(first):
            if first in arrays[i]:
                result.append(first) 
    return result



        

     


        
    






if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
