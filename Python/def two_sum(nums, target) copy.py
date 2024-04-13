def two_sum(nums, target):
  """
  Finds all pairs of elements in a list that add up to a target value.

  Args:
    nums: A list of integers.
    target: The target value.

  Returns:
    A list of all pairs of elements in nums that add up to target.
  """

  # Create a dictionary to store the elements of nums and their indices.
  num_dict = {}
  for i, num in enumerate(nums):
    num_dict[num] = i

  # Iterate over the elements of nums and check if their complements are in the
  # dictionary.
  result = []
  for i, num in enumerate(nums):
    complement = target - num
    if complement in num_dict and num_dict[complement] != i:
      result.append((i, num_dict[complement]))

  return result


# Example usage:

nums = [2, 7, 11, 15]
target = 9

print(two_sum(nums, target))