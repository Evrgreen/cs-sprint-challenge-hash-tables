def has_negatives(a):
    """
    YOUR CODE HERE
    """
    results = []
    numbers_seen = {}

    for num in a:
        numbers_seen[number] = 1
        if num != 0 and -num in numbers_seen:
            results.append(abs(num))

    return results
# Your code here


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
