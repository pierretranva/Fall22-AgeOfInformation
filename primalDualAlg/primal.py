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


def is_tight(c: int, data, currIndex: int, list_size: int):
    result = 0
    for i in range(1, currIndex):
        for j in range(currIndex, list_size):
            result += data[j].get_y()
        result *= data[currIndex].get_state()
    return result <= c


def primal_dual_alg(data: list):

    # cost value
    c = 2
    # constant theta
    theta = ((1 + 1 / c) ** c) - 1

    currIndex = 0
    # Iterates through each Slot in the list (from 1 to T inclusive)
    while currIndex < len(data):
        if data[currIndex].get_state() == 1: # state s(t) is equal to 1
            for i in range(0, currIndex):
                download_sum = 0
                # Gets the summation of d(t) from 1 to t (inclusive)
                for n in range(i, currIndex + 1):
                    download_sum += data[n].get_download()
                if download_sum < 1:
                    # z(t) = 1 - download_sum
                    data[currIndex].set_z(1 - download_sum)
                    # d(t) = d(t) + (download_sum / c) + (1 / theta * c)
                    data[currIndex].set_download(
                        data[currIndex].get_download()
                        + (1 / c) * download_sum
                        + (1 / (theta * c))
                    )
                    data[currIndex].set_y(1)
        else:  # state is not equal to 1
            for i in range(currIndex):
                if i < currIndex:
                    # z(t) = z(t-1)
                    data[i].set_z(data[i - 1].get_z())
                else:
                    # z(t) = 1
                    data[i].set_z(1)
        currIndex += 1
    # Correction: Variable y(t) when s(t) = 0 gets updated below at the end of slot T
    for i in range(len(data)):
        if data[currIndex].get_state() == 0: # state s(t) is equal to 0
            for j in range(currIndex):
                # if y "is not tight"
                if not is_tight(c, data, currIndex, len(data)):
                    data[currIndex].set_y(1)
        
    return data, c


def main():
    values = [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0]
    '''
    Used for Temporary Testing (Generating Random Values):
    for i in range(40):
        values.append(random.randint(0, 2))
    '''

    list_of_data = []
    for i in values:
        newSlot = Slot(i)
        list_of_data.append(newSlot)
    list_of_data, c = primal_dual_alg(list_of_data)
    print(total_cost(list_of_data, c))


if __name__ == "__main__":
    main()
