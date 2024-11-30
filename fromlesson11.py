################### lists ###################

array1=['a','b','c','d']
array2=['e','f','g']
array1.extend(array2) # = array1+=array3

array1.append('h')#add in the end
array1.append(['l','i'])#add in the end
array1.insert(2,'k')#add in the specfic index
array1.remove('k')#romve specfic item
#array1.clear()#remove all array
what_was_poped=array1.pop()#romve last item and can put the remove item in variable
print(array1.index('e'))# to know the index of specfic item

print(array1.count('a'))#to know number of specfic item

array1.sort()
print(array1)

array3=array1.copy()#pass by value
array4=array1#pass by refrence