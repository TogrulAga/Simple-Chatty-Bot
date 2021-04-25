A = int(input())
B = int(input())
H = int(input())

if H in range(A, B+1):
    print("Normal")
elif H < A:
    print("Deficiency")
else:
    print("Excess")
