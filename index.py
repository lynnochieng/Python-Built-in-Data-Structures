# Creating an empty list
my_list: list[int] = []

# Appending the elemeny
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Inserting the number
my_list.insert(1, 15)

# Extending the list
my_list.extend([50,60,70])

# Removing the last element
my_list.pop()

# Sorting
my_list.sort()

# Printing
index_of_30 = my_list.index(30)
print("The index of 30 in the list is:", index_of_30)
