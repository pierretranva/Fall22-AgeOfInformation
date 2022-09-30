from tkinter import W
from Slot import Slot

import random


def total_cost(data: list, c: int):
    cost: int = 0
    for slot in data:
        if slot.get_download() >= 1:
            cost += c
        elif random.random() <= slot.get_download():
            cost += c

    return cost


def online(data: list):
    # cost value
    c = 2
    # constant theta
    theta = ((1 + 1 / c) ** c) - 1
    # random number between [0,1)
    u = random.random()
    currIndex = 0
    while currIndex < len(data):
        if data[currIndex].get_state() == 1:
            for i in range(0, currIndex + 1):
                download_value = 0
                for j in range(0, currIndex + 1):
                    download_value += data[j].get_download()

                if download_value < 1:
                    sumationValue = 0
                    for o in range(i, currIndex + 1):
                        sumationValue += data[o].get_download() + (1 / (theta * c))
                    data[currIndex].set_download(
                        data[currIndex].get_download() + (sumationValue / c)
                    )
        data[currIndex].set_presum(data[currIndex].get_d_sum())
        data[currIndex].set_d_sum(
            data[currIndex].get_d_sum() + min(data[currIndex].get_download(), 1)
        )

        if data[currIndex].get_presum() <= u < data[currIndex].get_d_sum():
            u += 1
        else:
            pass
        currIndex += 1
    return data, c


def main():
    values = [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0]
    # for i in range(40):
    #     values.append(random.randint(0, 2))

    list_of_data = []
    for i in values:
        newSlot = Slot(i)
        list_of_data.append(newSlot)
    list_of_data, c = online(list_of_data)
    print(total_cost(list_of_data, c))


if __name__ == "__main__":
    main()
