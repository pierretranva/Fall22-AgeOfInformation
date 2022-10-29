from primalDualLearningAugmentedAlg.Package import *
import random
from scipy.stats import poisson
from scipy.stats import lomax

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

def primal_dual_learning_augmentation_alg(lambda: float, data: list, alpha: list, d: Int):
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
    lambda_values = [0.4, 0.6, 0.8, 1.0]
    distribution = ["Poisson", "Pareto"]
    selected_distribution = distribution[0]
    mean = 1
    D = 0 # Holds the distribution used in the PDLA
    if (selected_distribution == "Poisson"):
        D = poisson(mean)
    elif (selected_distribution == "Pareto"):
        pass # Will figure out later
    
    A_values = []
    for i in range(1, 1001):
        prob = random.uniform(0, 1)
        A_value.append(prob)

    d = 100 # Represents that we will split every second into 100 time units
    
    primal_dual_learning_augmentation_alg(lambda_values[random.randint(0, len(lambda_values)], D , A_values, d)

    return None


if __name__ == "__main__":
    main()
