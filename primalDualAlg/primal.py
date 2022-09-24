import Slot

def print_slot_contents(data: list):
    sum_d: int = 0
    for slot in data:
        sum_d += slot.get_download()
    return sum_d

def is_tight(c: int, data, currIndex: int, list_size: int):
    result = 0
    for i in range(1, currIndex):
        for j in range(currIndex, list_size):
            result += data[j].get_y()
        result *= data[currIndex].get_state()
    return result <= c

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
                
                # z(t) = 1 - download_sum
                data[currIndex].set_z(1 - download_value)

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
                data[i].set_z(data[i - 1].get_z())
            else:
                # z(t)=1
                data[i].set_z(1)
    for i in range(len(data)):
        if data[currIndex].get_state() == 0:
            for j in range(1, currIndex):
                # if y "is not tight"
                if not is_tight(c, data, currIndex, len(currIndex)):
                    data[currIndex].set_y(1)
    return data
    
def main():
    values = [1, 1, 0, 1, 1, 0, 0, 1, 0]
    list_of_data = []
    for i in values:
        newSlot = Slot(i)
        list_of_data.append(newSlot)
    list_of_data = primalDual(list_of_data)
    print_slot_contents(list_of_data)