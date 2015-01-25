#!/usr/bin/python

#INPUT: ints qi, qj, qrip, and matrix M of a GNFA
#OUTPUT: the new regex for the path between qi and qj
# after state qrip has been removed from the machine.
def arrow (qi, qj, qrip, M):
    r1 = M[qi][qrip]
    r2 = M[qrip][qrip]
    r3 = M[qrip][qj]
    r4 = M[qi][qj]
    return union(cat( cat(r1,star(r2)), r3), r4)

#INPUT: Strings A, B, representing regex in set notation
#OUTPUT: String of results of contatenating A and B.
#DETAILS: regular concat operation did not account for
# the empty set.
def cat(A,B):
    if A == "NOT" or B == "NOT":
        return "NOT"
    else:
        return A+B

#INPUT: String A, representing regex in set notation
#OUTPUT: String of result of Kleene star on A
def star(A):
    if A == "NOT":
        return ""
    else:
        if A[0:1] == "(":
            return A+"*"
        else:
            return "("+A+")*"

#INPUT: Strings A, B, representing regex in set notation
#OUTPUT: String of result of A union B
def union(A,B):
    if A == "NOT" and B == "NOT":
        return "NOT"
    elif A=="NOT" and B!="NOT":
        return B
    elif A!="NOT" and B=="NOT":
        return A 
    else:
        return "("+A+"U"+B+")"
    
#INPUT: an (n by n) matrix representing the dfa
#       which has row n-2 as the START and row n-1 as
#       the end states. All other states labels as they
#       would be in the DFA.
#OUTPUT: a regular expression which represents the
#       language
def regex(M):
    n = len(M)
    return regex_recursive(M, 0)[n-2][n-1]

#A recursive help function for the above function.
def regex_recursive(M, qrip):
    if qrip == len(M) - 2: return M
    else:
        L = [[ 0 for x in range(len(M))] for x in range(len(M))] 
        for x in range(len(M)):
                for y in range(len(M)):
                    L[x][y] = arrow(x,y, qrip, M)
        for x in range(len(M)):
            L[x][3] = "NOT"
            for y in range(len(M)):
                    L[4][y] = "NOT"
                    if x == qrip or y == qrip:
                        L[x][y] = "NOT"

        return regex_recursive(L,qrip+1)

#For interest's sake I ran the program
# on then GNFA represented below.
M=[
    ["NOT", "0", "1", "NOT", "NOT"],
    ["0", "NOT", "1", "NOT", "NOT"],
    ["1", "0", "NOT", "NOT", ""   ],
    ["" , "NOT", "NOT", "NOT", "NOT"],
    ["NOT", "NOT", "", "NOT", "NOT"]
    ]

if __name__ == "__main__":
    import regexSimplifyer
    print regexSimplifyer.clean(regex(M))
