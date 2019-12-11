# my_list = [1,2,3,4,5]
# print(my_list.pop(2))
# print(my_list[0])
# my_list[1:4] = [9,8,7]
# print(my_list)
# my_list.insert(2,7)
# print(my_list)
# del my_list[1:3]
# print(my_list)
# print(my_list.pop())
# print(my_list  + [6,6,6])
# list=['harry','aman','preet']
# list.append('jaggu')
# print(list)
# friends=['loog', 'bade_loog']
# list.append(friends)
# print(list)
list = [0,1,2,3,4,5,6,7,8,9]
list1 = []
list2 = []       

for i in list:
   if i%2 == 0:
       list1.append(i) 
       
for j in list:
    if j%2!=0:
       list2.append(j)
       
print(list1)
print(list2)