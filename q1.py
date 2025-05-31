def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        return -1

    # Swapping using only x and y
    x = x + y
    y = x - y
    x = x - y

    print("Swapped values:", x, y)
    
# Test case 1: One non-numeric value
result1 = swap("Apple", 10)  # Returns -1
print("Result 1:", result1)
    
# Test case 2: Both values numeric
result2 = swap(9, 17)        # Prints: Swapped values: 17 9
print("Result 2:", result2)