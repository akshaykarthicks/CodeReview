```python
def find_duplicates(nums):
    """
    Finds and returns a list of duplicate numbers in a given list.

    Args:
        nums: A list of numbers.

    Returns:
        A list containing only the duplicate numbers from the input list.  Returns an empty list if there are no duplicates.
    """
    seen = set()  # Use a set to efficiently track numbers we've seen
    duplicates = []  # Initialize an empty list to store duplicates

    for num in nums:  # Iterate through each number in the input list
        if num in seen:  # Check if the number is already in the 'seen' set
            duplicates.append(num)  # If it's already seen, it's a duplicate, add it to the duplicates list
        else:
            seen.add(num)  # If it's not seen, add it to the 'seen' set

    return duplicates  # Return the list of duplicate numbers

```

# README: Duplicate Number Finder

This Python code helps you identify duplicate numbers within a list.  It's designed to be easy to use, even if you're new to programming.

## What it does

The code takes a list of numbers as input and returns a new list containing only the numbers that appear more than once in the original list.

## Who it's for

This code is useful for anyone working with numerical data who needs to quickly find duplicate entries.  It's particularly helpful for data cleaning or analysis tasks.

## How it works

The code uses a set called `seen` to keep track of numbers encountered so far. A set is a data structure that only stores unique values.

1. **Initialization:** It starts with an empty set (`seen`) and an empty list (`duplicates`).
2. **Iteration:** It iterates through each number in the input list (`nums`).
3. **Duplicate Check:** For each number, it checks if the number is already present in the `seen` set.
   - If the number is in `seen`, it means it's a duplicate, so it's added to the `duplicates` list.
   - If the number is not in `seen`, it's added to the `seen` set to mark it as encountered.
4. **Return Value:** Finally, it returns the `duplicates` list, which contains all the duplicate numbers found.

## How to use it

1. **Copy the code:** Copy the `find_duplicates` function from above.
2. **Prepare your data:** Create a list of numbers. For example: `my_numbers = [1, 2, 3, 2, 4, 1, 5, 6, 3]`
3. **Call the function:** Pass your list to the `find_duplicates` function: `duplicate_numbers = find_duplicates(my_numbers)`
4. **View the results:** The `duplicate_numbers` variable will now contain a list of the duplicate numbers: `[1, 2, 3]`

## Example

```python
my_numbers = [1, 2, 3, 2, 4, 1, 5, 6, 3]
duplicates = find_duplicates(my_numbers)
print(f"The duplicate numbers are: {duplicates}")  # Output: The duplicate numbers are: [1, 2, 3]

empty_list = []
duplicates = find_duplicates(empty_list)
print(f"The duplicate numbers are: {duplicates}") #Output: The duplicate numbers are: []


no_duplicates_list = [1,2,3,4,5]
duplicates = find_duplicates(no_duplicates_list)
print(f"The duplicate numbers are: {duplicates}") # Output: The duplicate numbers are: []
```