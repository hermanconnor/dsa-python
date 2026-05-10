def bubble_sort(arr):
    """
    Sorts a list of elements in ascending order using the optimized Bubble Sort algorithm.

    This implementation includes a 'swapped' flag optimization, allowing it to 
    reach a best-case time complexity of O(n) if the list is already sorted.
    The sorting is performed in-place, modifying the original input.

    Args:
        arr (list): A list of comparable elements (e.g., integers, floats, strings).

    Returns:
        list: The same list object, now sorted.

    Complexity:
        Time: Best O(n), Average O(n^2), Worst O(n^2)
        Space: O(1) auxiliary.
    """
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr
