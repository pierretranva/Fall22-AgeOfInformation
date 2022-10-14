from tkinter import W
from Slot import *
import random


def total_cost(data: list, c: int):
    cost: int = 0
    for slot in data:
        if slot.get_download() >= 1:
            cost += c
        elif random.random() <= slot.get_download():
            cost += c
    return cost


def online_rand_alg(data: list, input_c: int):

    c = input_c
    # constant theta
    theta = ((1 + 1 / c) ** c) - 1
    # random number between [0,1) (so a double in the range of 0 and 1 exclusive)
    u = random.random()

    currIndex = 0
    # Iterates through each Slot in the list (from 1 to T inclusive)
    while currIndex < len(data):
        # state s(t) is equal to 1
        if data[currIndex].get_state() == 1:
            for i in range(0, currIndex + 1):
                download_sum = 0
                # Gets the summation of d(t) from 1 to t (inclusive)
                for j in range(i, currIndex + 1):
                    download_sum += data[j].get_download()

                if download_sum < 1:
                    # d(t) = d(t) + (download_sum / c) + (1 / theta * c)
                    data[currIndex].set_download(
                        data[currIndex].get_download()
                        + (download_sum / c)
                        + (1 / (theta * c))
                    )
        # d(t) [Presum] = d(t) [Currsum]
        data[currIndex].set_presum(data[currIndex].get_d_sum())
        # d(t) [Currsum] = d(t) [Currsum] + min(d(t), 1)
        data[currIndex].set_d_sum(
            data[currIndex].get_d_sum() + min(data[currIndex].get_download(), 1)
        )
        # if u is in-between the range of d(t) [Presum] and d(t) [Currsum]
        if data[currIndex].get_presum() <= u < data[currIndex].get_d_sum():
            u += 1
        else:
            # Denoting an "idle"/"passed" state
            pass
        currIndex += 1
    return data, c


def run_once():
    values = [1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1]
    # for i in range(100):
    #     values.append(random.randint(0,2))

    list_of_data = []
    for i in values:
        newSlot = Slot(i)
        list_of_data.append(newSlot)
    list_of_data, c = online_rand_alg(list_of_data)

    return total_cost(list_of_data, 15) / len(list_of_data)


def main():
    values = []
    input_c = 10
    """
    Used for Temporary Testing (Generating Random Values):
    """
    for i in range(100):
        # values.append(random.randint(1, 2))
        values.append(1)

    list_of_data = []

    for i in values:
        newSlot = Slot(i)
        list_of_data.append(newSlot)
    list_of_data, c = online_rand_alg(list_of_data, input_c)

    # total_amount = 0
    # for i in range(10):
    #     print(run_once())
    #     total_amount += run_once()
    # print(total_amount / 10)
    print(total_cost(list_of_data, input_c) / len(list_of_data))


if __name__ == "__main__":
    main()
