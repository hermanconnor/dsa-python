def bucket_sort_uniform(arr):
    """
      Sorts a list of floating-point numbers in the range [0, 1) using Bucket Sort.

      This version is optimized for uniformly distributed data. It maps each value
      directly to a bucket index based on its magnitude, bypassing the need to 
      calculate the global range.

      Args:
          arr (list[float]): A list of floats where each element x satisfies 0 ≤ x ≤ 1.

      Returns:
          list[float]: A new list containing the sorted elements.

      Complexity:
          Time: Average O(n + k), Worst O(n^2) (if all elements fall in one bucket).
          Space: O(n + k) where k is the number of buckets.
    """

    if len(arr) <= 1:
        return arr

    # Create buckets
    bucket_count = len(arr)
    buckets = [[] for _ in range(bucket_count)]

    # Distribute elements into buckets
    for num in arr:
        bucket_index = int(num * bucket_count)
        # Handle edge case where num = 1.0
        if bucket_index == bucket_count:
            bucket_index = bucket_count - 1
        buckets[bucket_index].append(num)

    # Sort individual buckets and concatenate
    sorted_arr = []
    for bucket in buckets:
        if bucket:
            bucket.sort()
            sorted_arr.extend(bucket)

    return sorted_arr
