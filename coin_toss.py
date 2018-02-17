import random
from collections import Counter
import matplotlib.pyplot as plt
import argparse
import math
from scipy.stats import norm
import numpy as np


def coin_toss(flips):
    """Return a list of 1s and 0s which correspond to coin tosses.
    Arguments:
    flips -- How many flips in total
    Returns:
    A list of [flips] coin toss results
    """
    return [x for x in [random.randint(0, 1) for x in range(flips)]]


def parse_arguments():
    """Parse command line arguments.
    Returns:
    flips -- The number of flips in one iteration
    iterations -- How many total iterations
    """
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-f', '--flips', type=int, help='number of flips',
                        default='100')
    parser.add_argument('-i', '--iterations', type=int,
                        help='number of iterations', default='1000')
    args = vars(parser.parse_args())
    flips = args['flips']
    iterations = args['iterations']
    return flips, iterations


def calculate_normal_dist(flips, iterations, step=0.1):
    """Calculates the x and y axis for coin toss normal distribution.
    Arguments:
    flips -- # of flips per iteration
    iterations -- # of total iterations
    step -- Step size for plotting (default=0.1)
    Returns:
    x and y axis for normal distribution with given params and step size
    """
    mean = flips/2.0
    # Probability of heads (or tails)
    p = 0.5
    n = flips
    variance = n * p * (1 - p)
    # Standard deviation
    std = math.sqrt(variance)
    # X-axis from 0 to [flips], between every [step]
    x_axis = np.arange(0, flips+1, step)
    return x_axis, norm.pdf(x_axis, mean, std)*iterations



def main():
    # Parse command line arguments
    flips, iterations = parse_arguments()
    print('Calculating distribution with {} flips and {} iterations'
          .format(flips, iterations))
    # List of sums of heads with [flips] flips, one sum for each iteration
    sums = [sum([x == 1 for x in coin_toss(flips)]) for x in range(iterations)]
    # Calculate the distribution of heads (or tails, makes no difference)
    dist = Counter(sums)

    # Calculate normal dist
    x_axis, y_axis = calculate_normal_dist(flips, iterations)
    # Plot the corresponding normal distribution
    plt.plot(x_axis, y_axis, 'r')

    # Plot results
    plt.bar(dist.keys(), dist.values())
    plt.xlabel('# of heads')
    plt.ylabel('# of times flipped x heads per {} iterations'
               .format(iterations))
    plt.title('Coin toss with {} flips and {} iterations'
              .format(flips, iterations))
    plt.show()


if __name__ == '__main__':
    main()
