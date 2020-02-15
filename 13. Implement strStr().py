'''
For a given source string and a target string, you should output the first
index(from 0) of target string in source string.

If target does not exist in source, just return -1.

Have you met this question in a real interview?  
Clarification
Do I need to implement KMP Algorithm in a real interview?

Not necessary. When you meet this problem in a real interview, the interviewer may just want to test your basic implementation ability. But make sure you confirm with the interviewer first.
Example
Example 1:

Input: source = "source" ，target = "target"
Output: -1  
Explanation: If the source does not contain the target content, return - 1.
Example 2:

Input:source = "abcdabcdefg" ，target = "bcd"
Output: 1   
Explanation: If the source contains the target content, return the location where the target first appeared in the source.
Challenge
O(n2) is acceptable. Can you implement an O(n) algorithm? (hint: KMP or RobinK)
'''

# TAG:[TWO INDICES, STRING, ROBIN-KARP, HASH]

# Solution 1 two pointers simulation O(n^2)
class Solution:
    """
    @param source: 
    @param target: 
    @return: return the index
    """
    def strStr(self, source, target):
        
        # corner cases
        if source is None or target is None:
            return -1
        if len(source) < len(target):
            return -1
        if len(target) == 0:
            return 0

        for i in range(len(source) - len(target) + 1):
            j = 0
            while j < len(target):
                if source[i + j] == target[j]:
                    j = j + 1
                else:
                    j = 0
                    break
            if j == len(target):
                return i

        return -1
# Takeaways:
# Two-indices manipulation

# Solution 2 Robin Karp O(n)
class Solution:
    """
    @param source: 
    @param target: 
    @return: return the index
    """
    
    def strStr2(self, source, target):
        BASE = 1000000
        
        # corner cases
        if source == None or target == None:
            return -1

        m = len(target)
        n = len(source)

        if m == 0:
            return 0

        # 31 ^ m
        power = 1
        for _ in range(m):
            power = (power * 31) % BASE;

        targetCode = 0
        for i in range(m):
            targetCode = (targetCode * 31 + ord(target[i])) % BASE

        hashCode = 0
        for i in range(n):
            # abc + d
            hashCode = (hashCode * 31 + ord(source[i])) % BASE
            if i < m - 1:
                continue

            # abcd - a
            if i >= m:
                hashCode = hashCode - (ord(source[i - m]) * power) % BASE
                if hashCode < 0:
                    hashCode += BASE
            
 
            # compare
            if hashCode == targetCode:
                if source[i - m + 1: i + 1] == target:
                    return i - m + 1
                

        return -1

# Takeaways:
# Remember how to select/slicing strings

'''
采用字符串哈希，字符串哈希时需要将字符串映射为数字，hash_target = (hash_target * 33 + target.charAt(i) - 'a') % mod;此处哈希函数，提供了字符串转化数字的关系式。
对于需要匹配的子串对应一个值，然后再遍历主串，当前位置为i，则用i的哈希值减去i-m部分的哈希值，求出中间m个长度的子串的哈希值，如果与要匹配串相同，由于哈希本身不安全，需要截取出来m长度的子串再进行匹配，完全相同即可。
注意负数取模时，需要通过+mod，将负数变为正数。
kmp是线性的字符串匹配算法，同样可以实现。
'''
