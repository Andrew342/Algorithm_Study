import sys

def palindrome_rec(str):
    if len(str)==1 or len(str)==0:
        return True
    else:
        if str[0]==str[-1]:
            return palindrome_rec(str[1:-1])
        else:
            return False

#print(palindrome_rec("kayak"))
print(palindrome_rec(str(sys.argv[1])))
