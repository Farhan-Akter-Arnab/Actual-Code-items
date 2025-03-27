A = {2, 3, 4}
B = {3, 8, 10}
C = {8, 10}
def comp(set_):
    if set_ == set():
        print("Ø")
    else:
        print(set_)
sett = A.symmetric_difference(B)
comp(sett)
sett = B.symmetric_difference(C)
comp(sett)
sett = A.symmetric_difference(C)
comp(sett)
sett = A.symmetric_difference(B.symmetric_difference(C))
comp(sett)
sett = B.symmetric_difference(A.symmetric_difference(C))
comp(sett)
sett = C.symmetric_difference(A.symmetric_difference(B))
comp(sett)
sett = A.intersection(B.intersection(C))
comp(sett)
sett = C.intersection(B.symmetric_difference(C))
comp(sett)