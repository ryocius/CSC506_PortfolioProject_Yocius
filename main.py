import random
from time import time
import matplotlib.pyplot as plt
from bst import Tree, BstNode
from hashtable import HashTable, HtNode

def hashBenchmark():
    output = {'insert': [], 'remove': [], 'search': []}

    # Build objects
    for i in range(1, 101):
        ht1 = HashTable()
        k = i * 100
        for j in range(k):
            ht1.add(HtNode(random.randint(1,100000), j))
        start_time = time()
        ht1.add(HtNode(5000, 5000))
        output['insert'].append(time() - start_time)

        start_time = time()
        ht1.search(5000)
        output['search'].append(time() - start_time)

        start_time = time()
        ht1.remove(5000)
        output['remove'].append(time() - start_time)

    return output


def bstBenchmark():
    output = {'insert': [], 'remove': [], 'search': []}

    # Build objects
    for i in range(1, 101):
        array = []
        k = i * 100
        for j in range(k):
            array.append(random.randint(1,100000))

        bst = Tree(array)

        start_time = time()
        bst.insert(5000)
        output['insert'].append(time() - start_time)

        start_time = time()
        bst.search(5000)
        output['search'].append(time() - start_time)

        start_time = time()
        bst.delete(bst.root, 5000)
        output['remove'].append(time() - start_time)

    return output

def showCombined(hashArray, bstArray):
    plt.plot(range(1, 101), hashArray['insert'], label='Hash Table Insert')
    plt.plot(range(1, 101), hashArray['remove'], label='Hash Table Delete')
    plt.plot(range(1, 101), hashArray['search'], label='Hash Table Search')
    plt.plot(range(1, 101), bstArray['insert'], label='BST Insert')
    plt.plot(range(1, 101), bstArray['remove'], label='BST Delete')
    plt.plot(range(1, 101), bstArray['search'], label='BST Search')
    plt.xlabel('Number of Samples (x100)')
    plt.ylabel('Time (s)')
    plt.title('Performance Comparison: Hash Table vs Binary Search Tree (BST)')
    plt.legend()
    plt.show()

def showHash(hashArray):
    plt.plot(range(1, 101), hashArray['insert'], label='Hash Table Insert')
    plt.plot(range(1, 101), hashArray['remove'], label='Hash Table Delete')
    plt.plot(range(1, 101), hashArray['search'], label='Hash Table Search')
    plt.xlabel('Number of Samples (x100)')
    plt.ylabel('Time (s)')
    plt.title('Performance: Hash Table')
    plt.legend()
    plt.show()

def showBst(bstArray):
    # Add search
    plt.plot(range(1, 101), bstArray['insert'], label='BST Insert')
    #plt.plot(range(1, 101), bstArray['remove'], label='BST Delete')
    plt.plot(range(1, 101), bstArray['search'], label='BST Search')
    plt.xlabel('Number of Samples (x100)')
    plt.ylabel('Time (s)')
    plt.title('Performance: Binary Search Tree')
    plt.legend()
    plt.show()

# showCombined(hashBenchmark(), bstBenchmark())
# showHash(hashBenchmark())
showBst(bstBenchmark())