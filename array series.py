def array_series(n):
    new_list = [0]*(n*n)
    group = n
    start = len(new_list)-1
    count = 1
    while(group > 0):
        while (count <= group):
            new_list[start] = count
            count = count+1
            start = start-1

        start = start - (n - group)
        group -= 1
        count = 1

    return new_list


if __name__ == "__main__":
    print(array_series(5))
