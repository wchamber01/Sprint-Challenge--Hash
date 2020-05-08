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
    for q in queries:
        if 'nofile' in q:
            continue
        if q in cache:
            if len(cache[q]) > 1:
                for i in q:
                    result.append(cache[q][i])
            else:
                result.append(cache[q])
        else:
            continue

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
