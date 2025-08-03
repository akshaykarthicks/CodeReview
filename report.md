```python
#This function finds duplicate numbers in a list.
def find_duplicates(nums):
    """
    Finds and returns a list of duplicate numbers in a given list.

    Args:
      nums: A list of numbers.

    Returns:
      A list containing only the duplicate numbers from the input list.  Returns an empty list if no duplicates are found.
    """
    seen = set() #Creates an empty set to store numbers we've already seen.  Sets are efficient for checking membership.
    duplicates = [] #Creates an empty list to store duplicate numbers.

    for num in nums: #Iterates through each number in the input list.
        if num in seen: #Checks if the current number is already in the 'seen' set.
            duplicates.append(num) #If it's already seen, it's a duplicate, so add it to the 'duplicates' list.
        else:
            seen.add(num) #If it's not seen yet, add it to the 'seen' set.

    return duplicates #Returns the list of duplicate numbers.

numbers = [1, 2, 3, 4, 2, 5, 6, 1]
print(find_duplicates(numbers)) # Output: [2, 1]

```

# README: Finding Duplicate Numbers in a List

This Python code provides a simple and efficient way to identify and extract duplicate numbers from a list.

## What it Does

The code takes a list of numbers as input and returns a new list containing only the numbers that appear more than once in the input list.

## Who it's For

This code is useful for anyone working with numerical data who needs to identify duplicates. This could include data analysts, programmers, or anyone working with datasets that might contain redundant entries.


## How it Works

The core logic uses a set called `seen` to keep track of numbers encountered so far.  A set is a data structure that only allows unique elements.

1. **Initialization:** An empty set `seen` and an empty list `duplicates` are created.
2. **Iteration:** The code iterates through each number in the input list.
3. **Duplicate Check:** For each number, it checks if the number is already present in the `seen` set.
   - If the number is in `seen`, it means it's a duplicate, so it's added to the `duplicates` list.
   - If the number is not in `seen`, it's added to the `seen` set to mark it as encountered.
4. **Return Value:** Finally, the function returns the `duplicates` list, which contains all the duplicate numbers found.


## How to Use It

1. **Save the Code:** Save the code above as a Python file (e.g., `find_duplicates.py`).
2. **Run from the Command Line:** Open your terminal or command prompt, navigate to the directory where you saved the file, and run it using the command `python find_duplicates.py`.
3. **Input:** The code includes an example list `numbers`. You can modify this list to test with your own data.
4. **Output:** The output will be a list of the duplicate numbers found in your input list.  For the example provided, the output is `[2, 1]` because 2 and 1 appear more than once in the input list `[1, 2, 3, 4, 2, 5, 6, 1]`.


## Example Usage

```
numbers = [1, 2, 3, 4, 2, 5, 6, 1]
duplicates = find_duplicates(numbers)
print(duplicates)  # Output: [2, 1]

numbers2 = [10, 20, 30, 40] #Example with no duplicates
duplicates2 = find_duplicates(numbers2)
print(duplicates2) # Output: []

```