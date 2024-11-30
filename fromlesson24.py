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

################# error handling ####################

try:
    result=10/0
    value=int(input("Enter a number: "))
    print(value)  # if first line in try has error the rest of the try dosn't operated
except ZeroDivisionError as err:
    print(err)
except ValueError as err2:
    print(err2)
print("sucess")
