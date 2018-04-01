def ordered_sequential_earch(a_list,item):
    pos=0
    found=False
    stop=False
    while pos<len(a_list) and not found and not stop:
        if a_list[pos]==item:
            found=True
        else:
            if a_list[pos]>item:
                stop=True
            else:
                pos=pos+1

    return found

test_list=sorted([1,2,32,8,17,19,42,13,0])
print(ordered_sequential_earch(test_list,3))
print(ordered_sequential_earch(test_list,13))
