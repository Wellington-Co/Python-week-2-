# empty list 
my_list = []

# Appending the elements 10, 20, 30, 40 to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Inserting the value 15 at the second position
my_list.insert(1, 15)

# Extending my_list with another list: [50, 60, 70]
my_list.extend([50, 60, 70])

# Removal of the last element from my_list
my_list.pop()

# Sorting my_list in ascending order
my_list.sort()

# printing the index of the value 30 in my_list
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)

# Printing the final list
print("Final list:", my_list)