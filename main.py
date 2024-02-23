import random
from time import time
import matplotlib.pyplot as plt
from bst import Tree, BstNode
from hashtable import HashTable, HtNode

def hashBenchmark():
    output = {'insert': [], 'remove': []}


    # Build objects
    for i in range(10):
        ht1 = HashTable()
        k = i * 100
        for j in range(k):
            ht1.add(HtNode(random.randint(1,100000), j))
        start_time = time()
        ht1.add(HtNode(5000, 5000))
        output['insert'].append(time() - start_time)

        start_time = time()
        ht1.remove(5000)
        output['remove'].append(time() - start_time)

    return output


def bstBenchmark():
    output = {'insert': [], 'remove': []}

    # Build objects
    for i in range(10):
        array = []
        k = i * 100
        for j in range(k):
            array.append(BstNode(random.randint(1,100000)))

        bst = Tree(array)

        start_time = time()
        bst.insert(BstNode(5000))
        output['insert'].append(time() - start_time)

        start_time = time()
        bst.delete(bst.root, 5000)
        output['remove'].append(time() - start_time)

    return output

def showCombined(hashArray, bstArray):
    plt.plot(range(1, 11), hashArray['insert'], label='Hash Table Insert')
    plt.plot(range(1, 11), hashArray['remove'], label='Hash Table Retrieve')
    # Add search
    plt.plot(range(1, 11), bstArray['insert'], label='BST Insert')
    plt.plot(range(1, 11), bstArray['remove'], label='BST Retrieve')
    plt.xlabel('Number of Samples (x100)')
    plt.ylabel('Time (s)')
    plt.title('Performance Comparison: Hash Table vs Binary Search Tree (BST)')
    plt.legend()
    plt.show()

def showHash(hashArray):
    plt.plot(range(1, 11), hashArray['insert'], label='Hash Table Insert')
    plt.plot(range(1, 11), hashArray['remove'], label='Hash Table Delete')
    # Add search
    plt.xlabel('Number of Samples (x100)')
    plt.ylabel('Time (s)')
    plt.title('Performance: Hash Table')
    plt.legend()
    plt.show()

def showBst(bstArray):
    # Add search
    plt.plot(range(1, 11), bstArray['insert'], label='BST Insert')
    plt.plot(range(1, 11), bstArray['remove'], label='BST Delete')
    plt.xlabel('Number of Samples (x100)')
    plt.ylabel('Time (s)')
    plt.title('Performance: Binary Search Tree')
    plt.legend()
    plt.show()

# showCombined(hashBenchmark(), bstBenchmark())
showHash(hashBenchmark())
# showBst(bstBenchmark())