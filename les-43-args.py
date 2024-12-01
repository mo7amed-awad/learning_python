def my_sum(a,b,*args,option):
    result=0
    if option:
        for x in args:
            result+=x
        return a+b+result
    else:
        return result
    # *args is like tuple
    # **kwargs is like dictionary
print(my_sum(1,2,3,4,5,option=9))  # must pass option by his name
