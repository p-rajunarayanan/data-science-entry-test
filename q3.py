def update_dictionary(dct, key, value):
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """
    if key in dct:
        print("Original value:", dct[key])
    dct[key] = value
    return dct
    
# Scenario 1: Adding a new key
result1 = update_dictionary({}, "name", "Alice")
print("Result 1:", result1)  # Expected: {'name': 'Alice'}

# Scenario 2: Updating an existing key
result2 = update_dictionary({"age": 25}, "age", 26)
print("Result 2:", result2)  # Expected: Original value: 25, then {'age': 26}