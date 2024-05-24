def extract_unique_values(input_dict):
    unique_values = set()
    for key in input_dict:
        value = input_dict[key]
        if isinstance(value, list):  # If the value is a list, iterate over it
            for item in value:
                unique_values.add(item)
        else:  # Otherwise, add the value directly
            unique_values.add(value)
    return unique_values

# Example dictionary
example_dict = {
    'a': 1,
    'b': 2,
    'c': 2,
    'd': 3,
    'e': [4, 5, 6],
    'f': [4, 7, 8]
}

# Extract unique values
unique_values = extract_unique_values(example_dict)
print(unique_values)