'''Given a string s and a set of n substrings. You are supposed to remove every
instance of those n substrings from s so that s is of the minimum length and output this minimum length.


Example 1:

Input:
"ccdaabcdbb"
["ab","cd"]
Output:
2
Explanation: 
ccdaabcdbb -> ccdacdbb -> cabb -> cb (length = 2)
Example 2:

Input:
"abcabd"
["ab","abcd"]
Output:
0
Explanation: 
abcabd -> abcd -> "" (length = 0)
'''

# TAG:[BFS, STR.FIND()]
# Solution 1 BFS
# Try to delete from every possible position, use bfs to find the best answer
class Solution:
    """
    @param: s: a string
    @param: dict: a set of n substrings
    @return: the minimum length
    """
    def minLength(self, s, dict):
        queue = collections.deque([s])
        unique = set([s])
        result = len(s)
        while queue:
            string = queue.popleft()
            for sub in dict:
                # the index that found
                found = string.find(sub)
                while found != -1:
                    new_s = string[:found] + string[found + len(sub):]
                    if new_s not in unique:
                        if (len(new_s)) < result:
                            result = len(new_s)
                        queue.append(new_s)
                        unique.add(new_s)
                    # might find another after the first occurrence
                    found = string.find(sub, found + 1)
        return result

# takeaways:
# find method -- str.find(sub, start(optional), end(optional)) return the first
# index of the sub string occurrence
 


