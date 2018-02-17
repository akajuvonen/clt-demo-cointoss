import random
from collections import Counter
import matplotlib.pyplot as plt
import argparse

def coin_toss(flips):
    """Return a list of 1s and 0s which correspond to coin tosses.
    Arguments:
    flips -- How many flips in total
    Returns:
    A list of [flips] coin toss results
    """
    return [x for x in [random.randint(0,1) for x in range(flips+1)]]

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

def main():
    # Parse command line arguments
    flips, iterations = parse_arguments()
    print('Calculating distribution with {} flips and {} iterations'
        .format(flips, iterations))
    # Calculate the distribution of heads (or tails, makes no difference)
    dist = Counter([x for x in [sum([x==1 for x in coin_toss(flips)]) for x in range(iterations)]])

    # Plot results
    plt.bar(dist.keys(), dist.values())
    plt.xlabel('# of heads')
    plt.ylabel('# of times flipped x heads per {} iterations'
        .format(iterations))
    plt.title('Coin toss with {} flips and {} iterations'
        .format(flips, iterations))
    plt.show()

if __name__=='__main__':
    main()
