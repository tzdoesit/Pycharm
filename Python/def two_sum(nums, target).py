def two_sum(nums, target):
  """
  Finds all pairs of numbers in a list that sum to a target value.

  Args:
    nums: A list of integers.
    target: The target value.

  Returns:
    A list of all pairs of numbers in nums that sum to target.
  """

  # Create a dictionary to store the numbers we've already seen.
  seen = {}

  # Iterate over the list.
  for i in range(len(nums)):
    # If the target minus the current number is in the dictionary,
    # then we've found a pair that sums to target.
    if target - nums[i] in seen:
      return [i, seen[target - nums[i]]]

    # Otherwise, add the current number to the dictionary.
    seen[nums[i]] = i

  # If we reach this point, then there are no pairs that sum to target.
  return []

# Example usage:

nums = [2, 7, 11, 15]
target = 9

print(two_sum(nums, target))