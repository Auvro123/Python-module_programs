def div(a,b):
    return a/b 

print(div(10,2))
print(div(3,1))
print(div(9,3))
def div(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("cannot divide by zero")

print(div(10,2))
print(div(3,0))
print(div(9,3))