

def find_kth_smallest_num(l,k):
    s=[]
    for i in range(k):
        res=float('inf')
        for item in l:
            if res>item:
                res,item=item,res
        if res==2:
            import pdb
            pdb.set_trace()
        if i!=k-1:
            l.remove(res)
        else:
            return l[0]


if __name__=="__main__":
    l=[1,2,3,4,5,6,7,8,9]
    k=3
    print("the {}th min num is {}".format(k,find_kth_smallest_num(l,k)))
