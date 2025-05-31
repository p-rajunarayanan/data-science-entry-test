def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    if not isinstance(s, str):
        return ""
    return s[::-1]
    
# Scenario 1
result1 = string_reverse("Hello World")
print("Result 1:", result1)  # Expected: "dlroW olleH"

# Scenario 2
result2 = string_reverse("Python")
print("Result 2:", result2)  # Expected: "nohtyP"