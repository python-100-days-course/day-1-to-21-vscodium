# tuples are similar to list, but are immutable or cannot be changed

my_tuple = (3, 6, 9)
print(my_tuple[2])

# to change can be converted to a list

new_list = list(my_tuple) # convert to a list to change
new_list[0] = 1
print(f"new_list = {new_list}")