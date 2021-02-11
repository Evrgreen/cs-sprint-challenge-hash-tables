def intersection(arrays):
    """
    YOUR CODE HERE
    """

    # Your code here
    tally = {}

    for arr in arrays:
        for num in arr:
            if num not in tally:
                tally[num] = 0

            tally[num] += 1

    result = [num for num, total in tally.items() if total == len(arrays)]

    return result


if __name__ == "__main__":
    # arrays = [[1, 2, 3, 4, 5], [1, 2, 3, 7, 8, 9]]
    arrays = []
    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
