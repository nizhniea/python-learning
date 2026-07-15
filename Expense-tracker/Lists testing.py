List = [12, 13, 14, 15, 16, 17, 18, 19, 20]
List.append(21)
print(List)
List_2 = [22, 23, 24, 25, 26, 27, 28, 29, 30]
List.extend(List_2)
print(List)
del List[0:4]
print(List)

X = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
print(f"X: {X}")
print(f"y: {y}")

X.extend(y)

Xy = X
del Xy[0:17:2]
len_X = len(Xy)
print(f"Xy: {Xy}")
print(f"Length of X: {len_X}")