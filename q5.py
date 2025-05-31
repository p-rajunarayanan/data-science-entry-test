def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    if not (isinstance(num, (int, float)) and isinstance(divisor, (int, float))):
        return False
    if divisor == 0:
        return False  # Prevent division by zero
    return num % divisor == 0
    
# Scenario 1: 10 divisible by 2
result1 = check_divisibility(10, 2)
print("Result 1:", result1)  # Expected: True

# Scenario 2: 7 not divisible by 3
result2 = check_divisibility(7, 3)
print("Result 2:", result2)  # Expected: False