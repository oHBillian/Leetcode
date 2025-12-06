# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal substring consisting of non-space characters only.

 

# Example 1:

# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
# Example 2:

# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
# Example 3:

# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.

# ก่อน refractor
s = "   fly me   to   the moon    "
# print(repr(s.rstrip()))
# def lengthOfLastWord(s):
#         if len(s) <= 1 and s != " ":
#             return len(s)
#         p = len(s) - 1
#         countString = 0
#         while True:
#             if (s[p] == " " and (p + 1 < len(s) and s[p + 1] != " ")) or p < 0:
#                 return countString
#             if s[p] != " ": countString += 1
#             p -= 1

# อันนี้ลอง REFRACTOR
def lengthOfLastWord2(s):
        string = s.rstrip()
        p = len(string) - 1
        countString = 0
        while True:
            if string[p] == " "  or p < 0:
                return countString
            countString += 1
            p -= 1
print(lengthOfLastWord2(s))

