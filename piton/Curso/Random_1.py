def has_pair_with_sum(arr, target):
    """
    Returns True if there are any two integers in the array arr whose sum is equal to target,
    and False otherwise.
    """
    # Create a set to store the values we've seen so far
    seen_values = set()

    # Iterate over each integer in the array
    for num in arr:
        # Check if there's a complement value in the set
        if target - num in seen_values:
            return True
        # Add the current value to the set of seen values
        seen_values.add(num)

    # If we've iterated over the whole array and haven't found a pair with the target sum, return False
    return False
    arr = [1, 2, 3, 4, 5]
    print(has_pair_with_sum(arr, 6))