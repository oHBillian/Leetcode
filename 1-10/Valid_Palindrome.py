# 125. Valid Palindrome

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after remo ving non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.

#ก่อน refractor
t = "A man, a plan, a canal: Panama" 
def Valid_Palindrome(s):
    if len(s) == 1:
        return True
    l, r = 0, len(s) - 1
    while r > l:
        # ทำเป็น 2 pointer เพื่อชี้ค่าแล้วเทียบกันไปเรื่อยๆถ้าเจอว่างจะเลื่อนตัวนั้นก่อนแล้วค่อยเทียบในรอบหน้่า
        if s[r].lower() == s[l].lower() and s[r].isalnum() and s[l].isalnum():
            r -= 1
            l += 1
            continue

        if not s[r].isalnum():
            r -= 1
            continue

        if not s[l].isalnum():
            l += 1
            continue

        if s[r].lower() != s[l].lower():
           return False

    return True

#หลัง refractor
def Valid_Palindrome2(s):
    if len(s) == 1:
        return True
    l, r = 0, len(s) - 1
    while r > l:
        if not s[r].isalnum():
            r -= 1
            continue

        if not s[l].isalnum():
            l += 1
            continue

        if s[r].lower() != s[l].lower():
           return False

        r -= 1
        l += 1

    return True
