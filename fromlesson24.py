friends=['esrra','safa','mariem']

for friend in friends:
    print(friend)

for x in range(10):
    print(x)

for friend in friends:
    if friend=="mohamed":
        print (friend)
        break
else:
    print("mohamed not found")


################## sets ######################
#is list but have uniqe items

#print(dir(friends))   #to know methods may apply to this type

name="mohamed"
unique_set=set(name)
print(unique_set)

