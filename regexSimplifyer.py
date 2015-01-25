import re

def clean (s):
    p = "\([0-9]*?\)(?!\*)"
    A = re.search(p, s)
    if A:
        A = A.group()
        B = A[1:-1]
        s = re.sub("\\("+B+"\\)", B, s)
        return clean(s)
    else:
        return s

#Test input:
# s = "(00U11)(0101)(1111)(0)*"
