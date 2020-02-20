'''
There is a new alien language which uses the latin alphabet. However, the
order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.
You may assume all letters are in lowercase.
The dictionary is invalid, if a is prefix of b and b is appear before a.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return the smallest in normal lexicographical order
Have you met this question in a real interview?  Yes
Problem Correction
Example
Example 1:

Input：["wrt","wrf","er","ett","rftt"]
Output："wertf"
Explanation：
from "wrt"and"wrf" ,we can get 't'<'f'
from "wrt"and"er" ,we can get 'w'<'e'
from "er"and"ett" ,we can get 'r'<'t'
from "ett"and"rftt" ,we can get 'e'<'r'
So return "wertf"

Example 2:

Input：["z","x"]
Output："zx"
Explanation：
from "z" and "x"，we can get 'z' < 'x'
So return "zx"
'''

# Solution 1 BFS
# 
# TAG:[BFS, PRIORITY QUEUE, HEAP, STRING]

# Remember to import this first
from heapq import heappush, heappop, heapify

class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alienOrder(self, words):
        # create a graph using the given words
        graph = self.build_graph(words)
        return self.topological_sort(graph)

    def build_graph(self, words):
        # node : neighbors
        graph = {}

        # put all the keys in
        for word in words:
            for c in word:
                if c not in graph:
                    graph[c] = set()

        # add neighbors
        n = len(words)
        for i in range(n - 1):
            for j in range(min(len(words[i]), len(words[i + 1]))):
                if words[i][j] != words[i + 1][j]:
                    graph[words[i][j]].add(words[i + 1][j])
                    break

        return graph

    def topological_sort(self, graph):
        indegree = self.get_indegree(graph)

        # Initialize first then do heapify
        pqueue = [node for node in graph if indegree[node] == 0]
        heapify(pqueue)

        order  = ""
        while pqueue:
            node = heappop(pqueue)
            order += node
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    heappush(pqueue, neighbor)

        if len(order) != len(graph):
            return ""
        return order

    def get_indegree(self, graph):
        # initialize
        indegree = {node : 0 for node in graph}
        for node in graph:
            for neighbor in graph[node]:
                indegree[neighbor] += 1
        return indegree

# Takeaways:
# Modularize all the functions
# Important step to know how to add the words to the graph: Simulation
# [List].append(node); (SET).add(); {Dict}[key] := value
# Familiarize the initialization of {} and []
# from heapq import heappush, heappop, heapify
