def isPalindrome(s):
    if len(s) == 1 or len(s) == 0:
        return True
    else:
        if s[0] == s[len(s)-1]:
            return isPalindrome(s[1:len(s)-1])
        else:
            return False
test_words = ["a", "nn", "racecar", "eye", "abfba", "abcfkcba", "12345654321", "123456654321", "god saw I was dog"]
for word in test_words:
    print(word, 'is a palindrome?', isPalindrome(word))