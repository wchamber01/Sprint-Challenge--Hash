def finder(files, queries):

    cache = {}
    result = []
    # [U]PER
    # loop through queries
    # if value not in d:

    #   -> add key with val as path

    # loop through files
    for q_str in queries:
        for path in files:
            if q_str in path:
                cache[q_str] = path
    print(cache)
    for q in queries:
        if q in cache:
            result.append(cache[q])

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
