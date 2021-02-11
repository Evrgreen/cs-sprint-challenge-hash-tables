# Your code here


def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    results = []
    cache = {}

    for file in files:
        filename = file.rsplit('/', 1)[1]
        if filename not in cache:
            cache[filename] = []
        cache[filename].append(file)

    for query in queries:
        if query in cache:
            results.extend(cache[query])
    return results


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/user/bar',
        '/user/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
