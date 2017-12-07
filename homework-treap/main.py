from Treap import Treap
import random
import matplotlib.pyplot as plt
import numpy as np

NUMBER_OF_TESTS = 100000
SIZE_OF_TREE = 100

def harmonic_sum(n):
    if n < 2:
        return 1
    else:
        return 1 / n + (harmonic_sum(n - 1))

def expectedDepth(n,k):
    """
        Returns the expected depth in a treap of size n for a number of rank k.
    """

    return harmonic_sum(k) + harmonic_sum(n-k+1) -1

if __name__ == "__main__":
    """
    We're gonna test on a range from 1 to 100 numbers, and each time add them randomly.
        Like a lot of times.
    """

    # TESTING
    expectance = [0]*SIZE_OF_TREE
    expected = [expectedDepth(SIZE_OF_TREE,i) for i in range(1,SIZE_OF_TREE+1)]

    for i in range(NUMBER_OF_TESTS):
        items = list(range(1,SIZE_OF_TREE+1))

        tree = Treap()
        for j in range(SIZE_OF_TREE):
            x = random.choice(items)
            del items[items.index(x)]
            tree.insert(x)

        for j in range(1,SIZE_OF_TREE+1):
            depth = tree.getDepth(tree.find(j))
            expectance[j-1] += depth

    for i in range(len(expectance)):
        expectance[i] /= NUMBER_OF_TESTS
        expectance[i] +=1
        print(expectance[i],expected[i])


    # PLOTTING
    t = np.arange(1.0, SIZE_OF_TREE+1.0, 1.0)
    print(t)
    expectance = np.array(expectance)
    expected = np.array(expected)

    plt.figure(1)
    plt.plot(t,expectance, label = "Tests")
    plt.plot(t,expected, label = "Expected")
    legend = plt.legend()
    plt.show()
