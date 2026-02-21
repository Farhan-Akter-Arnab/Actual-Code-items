class Node:
    def __init__(s,d): s.data=d; s.left=s.right=None
def p_sub(r,k):
    if r is None or k<=0: return
    if k==0: print(r.data,end=' '); return 0
    else: p_sub(r.left,k-1); p_sub(r.right,k-1)
def p_k(r,t,k):
    if r is None: return -1
    if r is t: p_sub(r,k); return 0
    dl=p_k(r.left,t,k)
    if dl!=-1:
        if dl+1==k: print(r.data,end=' ')
        else: p_sub(r.right,k-dl-2)
        return dl+1
    dr=p_k(r.right,t,k)
    if dr!=-1:
        if dr+1==k: print(r.data,end=' ')
        else: p_sub(r.left,k-dr-2)
        return dr+1
    return -1
def main():
    r=Node(10); r.left=Node(8); r.right=Node(12); r.left.left=Node(9); r.left.right=Node(11)
    t=r.left.right; k=2; print(f'Nodes at distance {k} from target ({t.data}):',end=' '); p_k(r,t,k); print()
if __name__=='__main__': main()