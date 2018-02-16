import random
from collections import Counter
import matplotlib.pyplot as plt

def coin_toss(flips):
    return [x for x in [random.randint(0,1) for x in range(flips)]]    

def main():
    flips = 100
    iterations = 1000
    dist = Counter([x for x in [sum([x==1 for x in coin_toss(flips)]) for x in range(iterations)]])
    plt.bar(dist.keys(), dist.values())
    plt.show()

if __name__=='__main__':
    main()
