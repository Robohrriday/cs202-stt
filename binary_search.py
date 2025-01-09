"""
This module contains the implementation of binary search algorithm.
"""

n = int(input("Enter the number of elements: "))
arr = []
for i in range(n):
    arr.append(int(input(f"Enter the element number {i}: ")))
ele = int(input("Enter the key to search: "))

def binary_search(a, key):
    """
    This function implements the binary search algorithm.
    Args:
        a: List of integers.
        key: Integer to search in the list.
    
    Returns:
        Index of the key in the list if found, otherwise -1.
    """
    low = 0
    high = len(a) - 1
    while low <= high:
        mid = (low + high) // 2
        if a[mid] == key:
            return mid
        if a[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

print(f"Index: {binary_search(arr, ele)}")

if __name__ == "__main__":
    print("Running Test Cases...")
    assert binary_search([1, 2, 3, 4, 5], 3) == 2
    assert binary_search([1, 2, 3, 4, 5], 5) == 4
    assert binary_search([1, 2, 3, 4, 5], 1) == 0
    assert binary_search([1, 2, 3, 4, 5], 6) == -1
    assert binary_search([1, 2, 3, 4, 5], 0) == -1
    assert binary_search([1, 2, 3, 4, 5], 2) == 1
    assert binary_search([1, 2, 3, 4, 5], 4) == 3
