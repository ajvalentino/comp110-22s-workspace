"""test"""

n: int = int(input("numba"))

if n % 3 != 0:
    print("C")
else:
    if n > 1:
        print("A")
    else:
        print("D")