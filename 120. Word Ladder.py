'''
Given two words (start and end), and a dictionary, find the shortest transformation sequence from start to end, output the length of the sequence.
Transformation rule such that:

Only one letter can be changed at a time
Each intermediate word must exist in the dictionary. (Start and end words do not need to appear in the dictionary )

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.

Example
Example 1:

Input：start = "a"，end = "c"，dict =["a","b","c"]
Output：2
Explanation：
"a"->"c"
Example 2:

Input：start ="hit"，end = "cog"，dict =["hot","dot","dog","lot","log"]
Output：5
Explanation：
"hit"->"hot"->"dot"->"dog"->"cog"
'''

# TAG:[BFS, GRAPH, SHORTEST PATH, IMPLICIT GRAPH]
# 
# Solution 1 BFS Traverse each layer

    #            lot -- log
    #           / |      |  \
    # hit -- hot  |      |   cog
    #          \  |      |  /
    #            dot -- dog
    #
    # 1       2   3     4     5

class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dict):
        dict.add(end)
        queue = collections.deque([start])
        visited = set([start])

        distance = 0

        while queue:
            distance += 1
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == end:
                    return distance

                for next_word in self.get_next_words(word):
                    # exceptions
                    if next_word not in dict or next_word in visited:
                        continue
                    queue.append(next_word)
                    visited.add(next_word)

        return 0

    # O(26 * L^2)
    # L is the length of the word
    def get_next_words(self, word):
        words = []
        for i in range(len(word)):
            # slit the words at the ith char
            left, right = word[:i], word[i + 1:]
            for char in 'abcdefghijklmnopqrstuvwxyz':
                if word[i] == char:
                    continue
                words.append(left + char + right)
        return words

# Takeaways:
# When popping out of the queue, we need to go to the next for level to get all
# the possible words that we can get

# Solution 2 BFS based on solution 1, use hashmap to store the distance save
# some time
class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dict):
        dict.add(end)
        queue = collections.deque([start])
        distance = {start : 1}

        while queue:
            word = queue.popleft()
            if word == end:
                return distance[word]

            for next_word in self.get_next_words(word):
                if next_word not in dict or next_word in distance:
                    continue
                queue.append(next_word)
                # if there exits word
                distance[next_word] = distance[word] + 1 

        return 0

    def get_next_words(self, word):
        words = []
        for i in range(len(word)):
            left, right = word[:i], word[i + 1:]
            for char in 'abcdefghijklmnopqrstuvwxyz':
                if word[i] == char:
                    continue
                words.append(left + char + right)
        return words

# Takeaways:
# Use hashMap: store the word and the same time the answer, reduce the time,
# increase the space



