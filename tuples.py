coordinates=(23,45)     #not changable / constant list
print(coordinates[1])

def say_hi():
    print('hi')

say_hi()

is_hungry = True

if is_hungry:
    print('go eat')

convert_month={
    "jan": "january",
    "feb":"febraury"
}

print(convert_month["jan"])
print(convert_month.get("feb"))
print(convert_month.get("not","default message"))
