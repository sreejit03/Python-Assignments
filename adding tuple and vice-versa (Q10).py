# Adding tuple to list
def add_tuple_to_list(my_list, my_tuple):
    my_list.append(my_tuple)
    return my_list

# Adding list to tuple
def add_list_to_tuple(my_tuple, my_list):
    new_tuple = my_tuple + tuple(my_list)
    return new_tuple

# Example usage
my_list = [(1, 2), (3, 4), (5, 6)]
my_tuple = (7, 8)

print("Original list:", my_list)
print("Original tuple:", my_tuple)

# Add tuple to list
my_list = add_tuple_to_list(my_list, my_tuple)
print("List after adding tuple:", my_list)

# Add list to tuple
my_tuple = add_list_to_tuple(my_tuple, [9, 10])
print("Tuple after adding list:", my_tuple)