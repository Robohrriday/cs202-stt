n = int(input("Enter the number of elements: "))
a = []
for i in range(n):
    a.append(int(input(f"Enter the element number {i}: ")))
key = int(input("Enter the key to search: "))

def binary_search(a, key):
    low = 0
    high = len(a) - 1
    while low <= high:
        mid = (low + high) // 2
        if a[mid] == key:
            return mid
        elif a[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

print(f"Index: {binary_search(a, key)}")

if __name__ == "__main__":
    print("Running Test Cases...")
    assert binary_search([1, 2, 3, 4, 5], 3) == 2
    assert binary_search([1, 2, 3, 4, 5], 5) == 4
    assert binary_search([1, 2, 3, 4, 5], 1) == 0
    assert binary_search([1, 2, 3, 4, 5], 6) == -1
    assert binary_search([1, 2, 3, 4, 5], 0) == -1
    assert binary_search([1, 2, 3, 4, 5], 2) == 1
    assert binary_search([1, 2, 3, 4, 5], 4) == 3
