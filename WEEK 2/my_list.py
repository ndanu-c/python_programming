my_list = []
my_list.append(10) #append first element
my_list.append(20) #append second element
my_list.append(30) #append third element
my_list.append(40) #append fourth element
my_list.insert(1, 15) #insert element at index 1
my_list.extend([50, 60, 70]) #extend list with multiple elements
del my_list[-1] #delete last element
my_list.sort() #sort the list

print(my_list.index(30)) #find index of element 30
print(my_list) # print the final list
