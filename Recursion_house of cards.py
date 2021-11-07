maxFloor = 0


def house_of_cards(num):
    global maxFloor
    if maxFloor < num:
        maxFloor = num

    totalCard = 0

    if num == 0:
        return "No house"

    if num == 1:
        totalCard += 8
        return totalCard

    if maxFloor > num:
        totalCard += 5

    totalCard = totalCard + 8 + house_of_cards(num-1)
    return totalCard


if __name__ == "__main__":
    print(house_of_cards(4))
