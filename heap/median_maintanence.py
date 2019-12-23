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

def rebalance_heap(min_heap, min_heap_size, max_heap, max_heap_size):
    # if min_heap larger than max_heap, take min_heap_max and add to the max_heap
    # if max_heap larger than max_heap, take max_heap_min and add to the min_heap

    if min_heap_size - max_heap_size > 1:
        min_val = max_heap.delMin()
        min_heap.insert(min_val)
    elif max_heap_size - min_heap_size > 1:
        max_val = min_heap.delMin()
        min_heap.insert(max_val)
    else:
        pass

    return min_heap, max_heap

def min_heap_insert(value, min_heap, min_heap_size):
    min_heap.insert(value)
    min_heap_max = min_heap.extract_max()
    min_heap_size += 1

    return min_heap, min_heap_max, min_heap_size

def max_heap_insert(value, max_heap, max_heap_size):
    max_heap.insert(value)
    max_heap_min = max_heap.extract_min()
    max_heap_size += 1

    return max_heap, max_heap_min, max_heap_size


def main():
    min_heap, max_heap = build_heaps()
    elements_added = 0
    min_heap_size = 0
    max_heap_size = 0

    min_heap_max = 0
    max_heap_min = 1000000000000

    elements_to_insert = [2, 7, 4, 2, 6, 9, 10, 11, 100, 50, 75, 23, 99, 15]

    for new_element in elements_to_insert:
        # add first element to min-heap
        if elements_added < 2:
            min_heap, min_heap_max, min_heap_size = min_heap_insert(new_element, min_heap, min_heap_size)
        elif new_element < min_heap_max:
            min_heap, min_heap_max, min_heap_size = min_heap_insert(new_element, min_heap, min_heap_size)
        else:
            max_heap, max_heap_min, max_heap_size = max_heap_insert(new_element, max_heap, max_heap_size)

        min_heap, max_heap = rebalance_heap(min_heap, min_heap_size, max_heap, max_heap_size)
        elements_added += 1


main()