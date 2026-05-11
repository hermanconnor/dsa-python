def bucket_sort(arr):
    """
    Sorts a list of numbers using the Bucket Sort algorithm.

    This implementation handles any range of numerical data by normalizing values
    relative to the minimum and maximum elements. It uses Python's built-in 
    Timsort for individual bucket sorting.

    Args:
        arr (list): A list of numerical elements (integers or floats).

    Returns:
        list: A new list containing the sorted elements.

    Complexity:
        Time: Average O(n + k), Worst O(n^2) or O(n log n) depending on bucket sort.
        Space: O(n + k) where n is the number of elements and k is the number of buckets.
    """

    if len(arr) <= 1:
        return arr

    # Find the maximum value to determine range
    max_val = max(arr)
    min_val = min(arr)

    # Handle case where all elements are the same
    if max_val == min_val:
        return arr

    # Create buckets - using same number of buckets as elements
    bucket_count = len(arr)
    buckets = [[] for _ in range(bucket_count)]

    # Distribute elements into buckets
    range_val = max_val - min_val
    for num in arr:
        # Calculate which bucket this number belongs to
        bucket_index = int((num - min_val) / range_val * (bucket_count - 1))
        buckets[bucket_index].append(num)

    # Sort individual buckets and concatenate
    sorted_arr = []
    for bucket in buckets:
        # Only sort non-empty buckets
        if bucket:
            bucket.sort()
            sorted_arr.extend(bucket)

    return sorted_arr
