list1=[1,2,3,4,5]
list2=['preet','ajay','harry','aman','mittu']
dict={1:list1,2:list2}
print(dict)
dict={list1:list2 for (list1,list2) in zip(list1,list2)}
print(dict)