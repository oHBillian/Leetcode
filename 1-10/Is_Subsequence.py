s = "abc"
t = "ahbgdc"

# ก่อน refractor
def isSubsequence(s, t): 
    p1 = 0
    p2 = 0
    newSrting = ''
    while p2 < len(t):
        if p1 < len(s) and s[p1] == t[p2]:
            newSrting += s[p1]
            p1 += 1
            p2 += 1
            continue
        p2 += 1
    return newSrting == s

# หลัง refractor
def isSubsequence(s, t): 
    p1 = 0
    p2 = 0
    newSrting = ''
    while p2 < len(t) and p1 < len(s):
        if s[p1] == t[p2]:
            newSrting += s[p1]
            p1 += 1
        p2 += 1
    return newSrting == s