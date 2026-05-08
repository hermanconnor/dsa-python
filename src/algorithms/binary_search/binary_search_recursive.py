def binary_search_recursive(arr, target, left=0, right=None):
    """
    Finds the index of a target element in a sorted array using recursion.

    This function implements the binary search algorithm, which divides the 
    search interval in half with each recursive call.

    Args:
        arr (list): A sorted list of elements (numeric or strings).
        target: The element to search for.
        left (int, optional): The starting index of the search range. 
            Defaults to 0.
        right (int, optional): The ending index of the search range. 
            If None, it is set to the last index of the array.

    Returns:
        int: The zero-based index of the target if found; -1 if the 
            target is not present in the array.
    """
    if right is None:
        right = len(arr) - 1

    # Base case: target not found
    if left > right:
        return -1

    mid = left + (right - left) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)
