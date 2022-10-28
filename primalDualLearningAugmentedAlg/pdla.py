from primalDualLearningAugmentedAlg.Package import *
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

def primal_dual_learning_augmentation_alg(data: list):
    lambda_values = []
    alpha_values = [[],[],[]]
    x: int = 0
    y: int = 0
    
    # for i in range(len(alpha_values)): # Traverse the times
    for j in range(len(lambda_values)): # Traverse for packages coming in
        sum: float = 0.00
        for k in range(i[j]):
            sum += k
            if(sum < 1):
                if(i >= a)
    
    return None

def main():
    lambda_values = [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0]
    '''
    Used for Temporary Testing (Generating Random Values):
    for i in range(40):
        values.append(random.randint(0, 2))
    '''
    '''
    list_of_data = []
    for i in values:
        newSlot = Slot(i)
        list_of_data.append(newSlot)
    list_of_data, c = primal_dual_alg(list_of_data)
    print(total_cost(list_of_data, c))
    '''
    pass
    

if __name__ == "__main__":
    main()
