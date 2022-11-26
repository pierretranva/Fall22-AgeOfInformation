import random
import math
import PDLA_Alg as PDLA
import DistributionFunctions as Dist
from PDLA_Alg import *


def main():
    lambdaValues = [0.4, 0.6, 0.8, 1.0]
    replacementRates = [
        0,
        0.05,
        0.1,
        0.15,
        0.20,
        0.25,
        0.30,
        0.35,
        0.40,
        0.45,
        0.50,
        0.55,
        0.6,
        0.65,
        0.7,
        0.75,
        0.8,
        0.85,
        0.9,
        0.95,
        1.0,
    ]
    distribution = ["Pareto", "Poisson"]
    numExperiments = 10
    d = 100
    meanDist = 1
    shape = 2
    lenTimeIntervals = 1000

    numIterations = 1

    # key = distribution[0] # Pareto Case
    key = distribution[1]  # Possion Case

    for prob in replacementRates:
        for i in range(numExperiments):
            distInstance = Dist.distrib_instance_gen(
                meanDist, lenTimeIntervals, numIterations, shape, key
            )
            (solution, OPT) = tcp_offline_alg(distInstance, d)

            for l in lambdaValues:
                LAPD = primal_dual_learning_augmentation_alg(
                    distInstance, d, l, solution
                )
                print(" Lambda = ", l, " CR = ", LAPD / OPT)

    return None  # Temporary Return Value (for now)


if __name__ == "__main__":
    main()
