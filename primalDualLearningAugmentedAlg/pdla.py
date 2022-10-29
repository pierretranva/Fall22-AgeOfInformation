from struct import pack
from primalDualLearningAugmentedAlg.Package import *
import random
from scipy.stats import poisson
from scipy.stats import lomax
import Package
import TimeSlot

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

def e(Lambda: float, d: int):
    return (1 + (1 / d)) ** (Lambda * d)

def primal_dual_learning_augmentation_alg(Lambda: float, data: list, alpha: list, d: int):

    if len(data) != len(alpha):
        raise Exception("data and alpha list inputs must have same number of items")

    for time in range(len(data)):  # Traverse the each time interval
        sum: float = 0.00
        for packages in range(len(data[time])):  # Traverse the packages in each time interval
            currTimeSlot: TimeSlot = TimeSlot(packages)
            sum += currTimeSlot.get_packages().get_x()
            if sum < 1:
                if time >= 1:  # t >= a(t(j)) - Will resolve later
                    for singPackageIndex in range(len(currTimeSlot.get_packages())):
                        currTimeSlot.get_packages_at_index(singPackageIndex).set_c(e(Lambda, d))
                        currTimeSlot.get_packages_at_index(singPackageIndex).set_c_prime(1 / d) 
                else:
                    for singPackageIndex in range(len(currTimeSlot.get_packages())):
                        currTimeSlot.get_packages_at_index(singPackageIndex).set_c(e(1 / Lambda, d))
                        currTimeSlot.get_packages_at_index(singPackageIndex).set_c_prime(Lambda / d)
                        
            packages.set_f(1 - sum)
            data[time].set_x((data[time].get_x() + (1 / d)) * (sum + (1 / (currTimeSlot.get_packages().get_c() - 1))))  # need to find out if c is a global variable
            packages.set_y(currTimeSlot.get_packages().get_c_prime())
    
    # if len(data) != len(alpha):
    #     raise Exception("data and alpha list inputs must have same number of items")

    # for time in range(len(data)):  # Traverse the each time interval
    #     sum: float = 0.00
    #     for packages in range(len(data[time])):  # Traverse the packages in each time interval
    #         sum += data[time][packages].get_x()
    #         if sum < 1:
    #             if 1 == 1:  # t >= a(t(j)) - Will resolve later
    #                 data[time][packages].set_c(e(Lambda, d))
    #                 data[time][packages].set_c_prime(1 / d)
    #             else:
    #                 data[time][packages].set_c(e(1 / Lambda, d))
    #                 data[time][packages].set_c_prime(Lambda / d)

    #         data[time][packages].set_f(1 - sum)
    #         data[time].set_x((data[time].get_x() + (1 / d)) * (sum + (1 / (data[time][packages].get_c() - 1))))  # need to find out if c is a global variable
    #         data[time][packages].set_y(data[time][packages].get_c_prime())
            
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
        A_values.append(prob)

    d = 100 # Represents that we will split every second into 100 time units
    
    primal_dual_learning_augmentation_alg(lambda_values[random.randint(0, len(lambda_values))], D , A_values, d)

    return None


if __name__ == "__main__":
    main()
