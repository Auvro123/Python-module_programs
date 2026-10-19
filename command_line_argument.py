import sys

print(sys.argv)
print(type(sys.argv))

arguments = sys.argv

a = int(arguments[1])
b = arguments[2]

print(a+int(b))