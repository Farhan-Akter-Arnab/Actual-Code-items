setx = {"black", "white"}
sety = {"black", "orange"}
seta = {"green", "blue"}
print("Original set elements: ")
print(setx)
print(sety)
print(seta)
print("\nIntersection of first two sets: ")
setz = setx.intersection(sety)
print(setz)
print("\nUnion of first two sets:")
setu = setx.union(sety)
print(setu)
print("\nIntersection of last two sets: ")
setz = seta.intersection(sety)
if setz == set():
    print("Ø")
print("\nUnion of last two sets:")
setu = seta.union(sety)
print(setu)
print("\nIntersection of first and third sets: ")
setz = setx.intersection(seta)
if setz == set():
    print("Ø")
print("\nUnion of first and third sets:")
setu = setx.union(seta)
print(setu)
print("\nIntersection of all sets: ")
seti = setx.intersection(sety.intersection(seta))
if seti == set():
    print("Ø")