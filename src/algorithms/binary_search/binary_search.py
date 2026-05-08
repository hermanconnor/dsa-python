def binary_search(arr, target):
    """
    Performs binary search on a sorted array to find the target element.

    Args:
        arr: Sorted list of elements to search through
        target: Element to search for

    Returns:
        int: Index of target element if found, -1 if not found
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
