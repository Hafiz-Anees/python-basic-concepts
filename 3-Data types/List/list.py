# nested list = [1,2,3,[4,5,6,[7,8,9]]]
# mixed list = [2,3,"anees",[5,6,7]]


print("\n----------LIST COMPREHENSION (HOW TO CREATE LIST)---------------------\n")

# 1sy way not good
# newlist = []
# for value in range(1,101):
#     newlist.append(value)

# print(newlist)

# 2nd way (better tha first one)

# print("\n\n")
# mylist = [x for x in range(1,50)]
# print(mylist)

# squares = [value**2 for value in range(1,11)]
# print(squares)

# print("\n")
# mylist = [x for x in range(1,50) if x%2==0]
# print(mylist)

# # converting string into list

# print("\n")
# myname = "anees ur rehman"
# s = [char for char in myname]
# print(s)

print("\n-------------------------LIST ITERAION-------------------------------\n")

# list1 = [22,1,3,5,67,45,89]

# # 1st way by indexing
# print("\n----------------------------------\n") 
# for i in range(len(list1)):
#     print(list1[i],end=" ")

# # 2nd by value
# print("\n----------------------------------\n") 
# for value in list1:
#     print(value,end=" ")

# print("\n----------------------------------\n") 

# n = len(list1)
# for n in range(n,0,-1):
#     print(list1[n-1],end=" ")



print("\n-----------------------------LIST METHODS--------------------------------\n")

list1 = [22,1,3,5,67,45,89]

# # sort

# list1.sort()
# print(list1)

# print("\n-------------------------------------------------------------------\n")

# # add at the end

# list1.append(0)
# print(list1)

# print("\n-------------------------------------------------------------------\n")

# # copy of the list
# newlist = list1.copy()
# print(newlist)

# print("\n--------------------------------------------------------------------\n")

# # count 
# list1.append(45)
# print(list1.count(45))

# print("\n--------------------------------------------------------------------\n")

# elements = [10,11,12,13]

# list1.extend(elements)
# print(list1)

# print("\n---------------------------------------------------------------------\n")

# index = list1.index(45)
# print("45 is first appear in the last at  index : ",index)

# print("\n---------------------------------------------------------------------\n")

# list1.insert(6,98)
# print(list1)

# print("\n---------------------------------------------------------------------\n")

# list1.remove(98)
# print(list1)

# print("\n---------------------------------------------------------------------\n")

# list1.reverse()
# print(list1)

# print("\n---------------------------------------------------------------------\n")

# del list1[4]
# print("After deleting element at index 4: ")
# print(list1)

print("\n---------------MULTPLE LIST ITERATION (ZIP FUNCTION)--------------------\n")

# l1 = [12,4,5,6,7,8,9,10]
# l2 = [1,2,3,4,5,6,7,8,9,10]
# print("L1","\t","L2")
# print("---","\t","---")
# for i,j in zip(l1,l2):
#   print(i,"\t",j)  # ITERATE BY FOLLOWING THE LENGHT  OF SHORTEST LIST