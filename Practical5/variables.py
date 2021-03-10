a = 060103
b = 190784
c = 100321
d = abs(a - c)
e = abs(b - c)
if d - e > 0:
    print('d is greater')
else:
    print('e is greater')

X = bool(input("value of X (0 or 1):"))
Y = bool(input("value of Y (0 or 1):"))
Z = (X and not Y) or (Y and not X)
print(Z)
W = (X!=Y)
print(W)
