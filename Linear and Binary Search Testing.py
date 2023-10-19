import time
import functools
import random

l1 = [12, 32, 43, 54, 1, 2, 7, 8, 12, 11, 10,5,3,4]
l1 = set(l1)
l1 = list(l1)
l1.sort()
# print(l1)


def timer(fn):
    @functools.wraps(fn)  # this keeps the identity of the original function being decorated when you print out the function
    def wrapper(*args, **kwargs):
        s_time = time.perf_counter()
        rv = fn(*args, **kwargs)
        e_time = time.perf_counter()
        elapsed_time = e_time - s_time
        print(f"{fn.__name__} ran in {elapsed_time}")
        return rv
    return wrapper

@timer
def binary_search(*, array, target): #returns the index or the target 
    # sort list
    array = set(array)
    array = list(array)
    array.sort()

    low_idx = 0
    high_idx = len(array)-1
    if array[low_idx] == target:
            return 0
    elif array[high_idx] == target:
        return len(array)-1
    else:
        while(low_idx <= high_idx):
            mid_idx = (low_idx + high_idx) // 2
            mid_item = array[mid_idx]
            if mid_item == target:
                return mid_item
            if mid_item < target:
                low_idx = mid_idx + 1
            if mid_item > target:
                high_idx = mid_idx - 1
        return None #returns None if the target does not exist

@timer
def linear_search(*, array, target, sort_list=True):
    if sort_list:
        # sort list
        array = set(array)
        array = list(array)
        array.sort()

    for i in array:
        if i == target:
            return i


# short list test
print(binary_search(array=l1, target=12))
print(linear_search(array=l1, target=12))

print("*"*80)

# larger list test
#Generate 5 random numbers between 10 and 30
# randomlist = random.sample(range(0, 1000), 1)
random_list = list(range(0, 1000))
# print(random_list)

print(binary_search(array=random_list, target=524))
print(linear_search(array=random_list, target=524))
