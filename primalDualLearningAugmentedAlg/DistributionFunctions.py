import random
import math
import numpy as np

def entry_gen(mean, n, shape, key):
    if(key == "Pareto"):
        return round(np.random.pareto(shape))
    elif(key == "Poisson"):
        dist = mean
        for i in range(n):
            dist = np.random.poisson(dist)
        return dist
    else:
        return None

def distrib_instance_gen(mean, length, numIterations, shape, key):
    instance_list = []

    for i in range(length):
        x = entry_gen(mean, numIterations, shape, key)
        for j in range(x):
            instance_list.append(i)
    
    return instance_list

def agg_instance(instance):
    sorted_ins = sorted(instance)

    if(len(instance) == 0):
        return []

    minTime = instance[0]
    maxTime = instance[len(instance) - 1]

    aggregatedInstance = [0] * minTime

    curr = 0
    for time in range(minTime, maxTime + 1):
        aggregatedInstance.append(0)

        while(curr < len(instance) and instance[curr] == time):
            aggregatedInstance[time] += 1
            curr += 1
    
    return aggregatedInstance

def deagg_instance(instance):
    result = []

    for i in range(len(instance)):
        for x in range(instance[i]):
            result.append(i)
    
    return result