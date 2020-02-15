'''
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Assume the length of given string will not exceed 100000.

Example 1:

Input : s = "abccccdd"
Output : 7
Explanation :
One longest palindrome that can be built is "dccaccd", whose length is `7`.
'''
# TAG:[HASH, STRING, ASCII, CONVERT DATATYPE]
# 
class Solution:
    # @param {string} s a string which consists of lowercase or uppercase letters
    # @return {int} the length of the longest palindromes that can be built
    
    # the answer is the count of characters that has even number of appereances.
    # for characters that has odd number of appereances,
    # their appereances minus 1 will make their apperances even.
    # And finally we can put an unused character in the middle of the palindrome
    def longestPalindrome(self, s):
        hash = {}
        
        for c in s:
            if c in hash:
                del hash[c] # remove key value pair
            else:
                hash[c] = True
                
        remove = len(hash)
        if remove > 0: # if there are additional char
            remove -= 1
        
        return len(s) - remove

# Takeaway
# Remove key-value pair in the hash
# Simulate the process!


'''
Follow-up: !!
print out the longest palindrome.with sequential order(smallest string ASCII)
'''
class Solution:
    # @param {string} s a string which consists of lowercase or uppercase letters
    # @return {string} the length of the longest palindromes that can be built
    
    def longestPalindrome(self, s):
        if not s:
            return ""
        # Best way to create a list full of 0
        # Total number of ASCII is 256
        hashTable = [0 for i in range(256)]

        # s = 'aaababcdcc'
        for c in s:
            hashTable[ord(c) - ord('A')] += 1
        # {a: 4, b: 2, c: 3, d: 1}
        
        # print(hashTable)
        ans = ""
        # flag if puts the last oddchar in the ans
        oddchar = -1

        for i in range(256):
            # half of the times that char appeared and then append
            times = hashTable[i] / 2
            for j in range(times):
                ans += chr((ord('A') + i))
            if hashTable[i] % 2 == 1 and oddchar == -1:
                # smallest char
                oddchar = chr(ord('A') + i)
        
        # ans = "aabc"
        half = len(ans)

        if (oddchar != -1):
            ans += oddchar
        
        # ans = "aabcc"
        
        # How to use range to reverse the index
        for i in range(half - 1, -1, -1):
            ans = ans + ans[i]
        
        return ans

# Takeaways:
# Total number of ASCII is 256
# 'A' : 65 -- smallest alphabet in ASCII
# hashTable = [0 for i in range(256)]
# ord(char) -- convert a char to int
# chr(int)  -- convert an int to char
# string concatenation     str += another char or another str
# use range() to reverse -- range[from, to), -1(reverse))