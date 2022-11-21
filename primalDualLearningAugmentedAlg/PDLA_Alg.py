import math

def determine_total_cost(instance, d, solution):
    cost = 0
    currJobs = []

    sortedInstance = sorted(instance)
    sortedSolution = sorted(solution)

    for request in sortedInstance:
        currJobs.append((request, math.inf))
    
    count = 0
    for times in solution:
        while(i < len(currJobs) and currJobs[i][0] <= times):
            currJobs[i] = (currJobs[i][0] <= times)
            count += 1

    for job in currJobs:
        cost += (1 / d) * (currJobs[1] - currJobs[0])
    
    return (cost + len(solution))

def primal_dual_learning_augmentation_alg(instance, d, lambdaVal, heurTimeList):
    # TO BE CONTINUED...
    return None

def tcp_offline_alg(instance, d):
    # TO BE CONTINUED...
    return None