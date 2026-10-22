import io

filename = "file.txt"
mode ="r"

try:
    with open(filename,mode) as fp:
        content = fp.read()
        print(content)
except FileNotFoundError:
    print(filename,"not found . check this name")
except io.UnsupportedOperation:
    print("are you sure ",filename,"is readble????????????????")