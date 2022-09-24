import Slot


def primalDual(data: list):
    # d(t)
    download = None
    # z(t)
    zIndex = None
    # y(t)
    y = 0
    # cost of downloading
    c = 2
    # constant theta
    theta = ((1 + 1 / c) ** c) - 1

    currIndex = 0
    if data[currIndex].get_state() == 1:
        for i in range(0, currIndex):
            download_value = 0
            for n in range(i, currIndex):
                download_value += data[n].get_download()
            if download_value < 1:
                # need to add z(t) line
                data[currIndex].set_download(
                    data[currIndex].get_download()
                    + (1 / c) * download_value
                    + (1 / (theta + c))
                )
                data[currIndex].set_y(1)
    else:  # state is not equal to 1
        for i in currIndex:
            if i < currIndex:
                # z(t) = z(t-1)
                pass
            else:
                pass
                # z(t)=1


def main():
    values = [1, 1, 0, 1, 1, 0, 0, 1, 0]
    list_of_data = []
    for i in values:
        newSlot = Slot(i)
        list_of_data.append(newSlot)
    primalDual(list_of_data)
