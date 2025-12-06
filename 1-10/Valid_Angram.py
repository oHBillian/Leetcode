# 242. Valid Anagram

# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false


a = "aacc"
b =  "ccac"
def Valid_Angram(s,t):
    # ทำ hash map เก็บตัวอักษรนั้นๆพร้อมบวกค่าพื่อเอามาเทียบภายหลัง
    if len(s) != len(t):
        return False

    stringA, stringB = {}, {}
    
    for i in range(len(s)):
        stringA[s[i]] = 1 + stringA.get(s[i], 0)
        stringB[t[i]] = 1 + stringB.get(t[i], 0)    

    for i in stringA:
        if stringA.get(i, 0) != stringB.get(i, 0):
            return False

    return True