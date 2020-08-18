def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    negative_numbers = {}

    for numbers in a:
        negative_numbers[numbers] = -numbers

    result = []

    for number in negative_numbers.keys():
        if number > 0 and negative_numbers[number] in negative_numbers:
            result.append(number)

    return result

   


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
