# Tuples in Python are an immutable and ordered collection of elements.
# They are similar to lists but cannot be changed after creation,
# making them useful for storing data that should not be modified.
# Tuples are created by placing elements inside parentheses () separated by commas.

# Key Characteristics of Tuples:
# Immutable: Once a tuple is created, its elements cannot be modified.
# Ordered: The elements have a defined order that will not change.
# Allow Duplicates: Tuples can contain duplicate elements.
# Heterogeneous: Tuples can store elements of different data types.


# Creating a tuple
my_tuple = (1, 2, 3, "apple", "banana")

# Accessing elements
print(my_tuple[0])  # Output: 1
print(my_tuple[3])  # Output: apple

# Slicing a tuple
print(my_tuple[1:4])  # Output: (2, 3, 'apple')

# Tuple length
print(len(my_tuple))  # Output: 5

# Nested tuples
nested_tuple = (1, (2, 3), (4, 5))
print(nested_tuple[1])  # Output: (2, 3)

# Iterating through a tuple
for item in my_tuple:
    print(item)
