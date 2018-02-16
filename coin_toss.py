import random
from collections import Counter
import matplotlib.pyplot as plt
import argparse

def coin_toss(flips):
    return [x for x in [random.randint(0,1) for x in range(flips+1)]]    

def parse_arguments():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-f', '--flips', type=int, help='number of flips', default='100')
    parser.add_argument('-i', '--iterations', type=int, help='number of iterations', default='1000')
    args = vars(parser.parse_args())
    flips = args['flips']
    iterations = args['iterations']
    return flips, iterations

def main():
    flips, iterations = parse_arguments()
    print('Calculating distribution with {} flips and {} iterations'.format(flips, iterations))
    dist = Counter([x for x in [sum([x==1 for x in coin_toss(flips)]) for x in range(iterations)]])
    plt.bar(dist.keys(), dist.values())
    plt.show()

if __name__=='__main__':
    main()
