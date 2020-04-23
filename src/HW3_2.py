def isPalindrome(s):
    if len(s) == 1 or len(s) == 0:
        return True
    else:
        if s[0] == s[len(s)-1]:
            return isPalindrome(s[1:len(s)-1])
        else:
            return False
def tolower(s):
    return s.lower()
def findPalindrome(s):
    return list(filter(isPalindrome, map(tolower, s)))
test_words = ["raCecar", "YeEy", "Eye", "LisaBonetAteNoBasil", "God saw I was dog", "palindrome"]
print (findPalindrome(test_words))