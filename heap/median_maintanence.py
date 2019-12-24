# Get a sequence of numbers one by one
# At each step i return the median of numbers received so far
# Use O(log i) time at each step


# Import graph class
from heap_utility import Min_Heap, Max_Heap

# low_heap => supports extract max
# high_heap => supports extract min
# Note that if the heaps are balanced then the median is either the max-of-the-low-heap or the min-of-the-high-heap
# (or an average of the two)


# check where the new element lies WRT low_heap max and high_heap min
# might need to rebalance as time goes on

def build_heaps():
    min_heap = Max_Heap()
    max_heap = Min_Heap()
    return min_heap, max_heap

def rebalance_heap(min_heap, max_heap):
    # if min_heap larger than max_heap, take min_heap_max and add to the max_heap
    # if max_heap larger than max_heap, take max_heap_min and add to the min_heap

    if min_heap.currentSize - max_heap.currentSize > 1:
        # Take from min heap and put into max heap
        max_val = min_heap.delMax()
        max_heap.insert(max_val)
    elif max_heap.currentSize - min_heap.currentSize > 1:
        # take from max heap and put in min heap
        min_val = max_heap.delMin()
        min_heap.insert(min_val)
    else:
        pass

    # If the min value of heap1 is greater than the max value of heap 2, then swap them...

    if min_heap.currentSize > 0 and max_heap.currentSize > 0 and (min_heap.extract_max() > max_heap.extract_min()):
        max_val = min_heap.delMax()
        min_val = max_heap.delMin()
        max_heap.insert(max_val)
        min_heap.insert(min_val)

    return min_heap, max_heap

def min_heap_insert(value, min_heap):
    min_heap.insert(value)
    min_heap_max = min_heap.extract_max()

    return min_heap, min_heap_max

def max_heap_insert(value, max_heap):
    max_heap.insert(value)
    max_heap_min = max_heap.extract_min()

    return max_heap, max_heap_min


def main():
    min_heap, max_heap = build_heaps()
    elements_added = min_heap.currentSize + max_heap.currentSize

    min_heap_max = 0
    median = 0

    print('min size: ', min_heap.currentSize)

    elements_to_insert = [2, 7, 4, 2, 6, 9, 10, 11, 100, 50, 75, 23, 99, 15]

    for new_element in elements_to_insert:
        print("adding element")
        # add first element to min-heap
        if elements_added < 2:
            min_heap, min_heap_max = min_heap_insert(new_element, min_heap)
        elif new_element < min_heap_max:
            min_heap, min_heap_max = min_heap_insert(new_element, min_heap)
        else:
            max_heap, max_heap_min = max_heap_insert(new_element, max_heap)


        min_heap, max_heap = rebalance_heap(min_heap, max_heap)
        elements_added += 1


        if min_heap.currentSize > max_heap.currentSize:
            median = min_heap.extract_max()
        elif min_heap.currentSize < max_heap.currentSize:
            median = max_heap.extract_min()
            print("min of max heap is ", median)
        elif min_heap.currentSize == max_heap.currentSize:
            print("min of max heap is ", max_heap.extract_min(), ' max of min heap is: ', min_heap.extract_max())
            median = int((max_heap.extract_min() + min_heap.extract_max())) / 2

        print('min size: ', min_heap.currentSize, ' max size: ', max_heap.currentSize)
        print('inserted value was: ', new_element, ' median is: ', median)


main()