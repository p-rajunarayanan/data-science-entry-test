def find_first_negative(lst):
    """
    Task 1
    - Create a function that finds the first negative number in a list (lst).
    - Return the first negative number if found, otherwise return "No negatives".
    - Use a while loop to implement this.
    """
    i = 0
    while i < len(lst):
        if lst[i] < 0:
            return lst[i]
        i += 1
    return "No negatives"
   
# Scenario 1: Contains negatives
result1 = find_first_negative([3, 5, -1, 7, -2, 8])
print("Result 1:", result1)  # Expected: -1

# Scenario 2: No negatives
result2 = find_first_negative([2, 10, 7, 0])
print("Result 2:", result2)  # Expected: "No negatives"