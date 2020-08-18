# dict ={}
# def single_list(arr):
#     for i in range(len(arr)):
#         dict[i]=arr[i]
#     return dict 


def intersection(arrays):
    """
    YOUR CODE HERE
    """
    result = []
    for array in arrays:
        for arr in array:
            result1[arr] = arr
            if result1[arr] == arr:
                result.append(arr)

    return result
    # dict_arrays={}
    # for index in range (len(arrays)):
    #     dict_arrays[i]=arrays[i]

    # first = arrays[0] 

    # for i in 
        

    # dict2={}
    # first=arrays[0]
    # result = []
    # for i in range(len(arrays)):
    #     dict2[i]=arrays[i] 

    # for i in range(len(first)):
    #     for j in range(len(arrays)):
    #         if first[i] in arrays[j]:
    #             result.append(first[i])
    # return result    


        
    






if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
