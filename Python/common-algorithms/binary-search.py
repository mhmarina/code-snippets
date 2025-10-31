import math

# find x in array using binary search
def binary_search(array, x, start, end):
    if end < start:
        return False
    
    mid = math.floor((end+start)/2)

    if array[mid] < x:
        return binary_search(array, x, mid+1, end)
    elif array[mid] > x:
        return binary_search(array, x, start, mid-1)
    elif array[mid] == x:
        return True   
     
if __name__ == "__main__":
    test_odd = [10,200,13,45,6,7,9,111,23,4,56,89,303,2,1,2,0,23]
    test_odd.sort()
    n = len(test_odd)-1
    print(len(test_odd))
    print(binary_search(test_odd, 200, 0, n))
    print(binary_search(test_odd, 111, 0, n))
    print(binary_search(test_odd, 83930, 0, n))
    print(binary_search(test_odd, 2, 0, n))
    print(binary_search(test_odd, 0, 0, n))

    test_even = [0,2,3,5]
    test_even.sort()
    n = len(test_even)-1
    print(binary_search(test_even, 2, 0, n))
    print(binary_search(test_even, 8, 0, n))