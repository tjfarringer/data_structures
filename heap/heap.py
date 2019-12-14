# In order to make our heap work efficiently, we will take advantage
# of the logarithmic nature of the binary tree to represent our heap.
# In order to guarantee logarithmic performance, we must keep our tree balanced.

# Usually represented via a list

# We will begin our implementation of a binary heap with the constructor.
# Since the entire binary heap can be represented by a single list,
# all the constructor will do is initialize the list and an attribute currentSize to keep track of the current size of the heap.


# Key property in a heap:  In a heap, for every node 𝑥 with parent 𝑝, the key in 𝑝 is smaller than or equal to the key in 𝑥
# The parent of the current node can be computed by dividing the index of the current node by 2.

class Heap():
    def __init__(self):
     self.heapList = [0]
     self.currentSize = 0

    def percolateUp(self, i):
        while i // 2 > 0: # allow for the possibility to go all the way up the tree
            if self.heapList[i // 2] > self.heapList[i]:
                self.heapList[i], self.heapList[i // 2] =  self.heapList[i // 2], self.heapList[i]
            i = i // 2

    def percolateDown(self, i):
        while i * 2 <= self.currentSize: # allow for the possibility to go all the way down the tree
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                self.heapList[i], self.heapList[mc] =  self.heapList[mc], self.heapList[i]
            i = i * 2

    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    def insert(self, k):
        self.heapList.append(k)
        self.currentSize += 1
        self.percolateUp(self, self.currentSize) # want to pass the index of k, which is equal to the currentSize of the heap

    def delMin(self):
        '''
        Smallest element is the min.  Hard part is restoring the tree afterwards.

        Two steps to fix:
        1. restore the root item by taking the last item in the list and moving it to the root position
        2. restore the heap order property by pushing the new root node down the tree to its proper position
        :return:
        '''
        min_val = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval

    def buildHeap(self, alist):
        '''
        Builds a heap from a list
        :param alist:
        :return:
        '''
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i = i - 1