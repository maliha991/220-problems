counter = 1


def random(k, length):
    global counter
    value = (counter + k) % length
    print("counter: ", counter, "K: ", k)
    counter += k
    return value


if __name__ == "__main__":
    values = [i for i in range(3+1)]
    while(counter < 30):
        for i in values:
            print(random(i, len(values)))
