def removeAll(source, size, element):
    twos = 0
    for k in range(size):
        if source[k] == element:
            source[k] = 0
            twos += 1

    i = 0
    nonZeros = size - twos
    while(i < nonZeros):

        if source[i] == 0:
            for j in range(i+1, size):
                source[j-1] = source[j]
        else:
            i += 1

    return source


if __name__ == "__main__":
    source = [10, 2, 2, 30, 2, 50, 2, 2, 0, 0]
    print(removeAll(source, 8, 2))
