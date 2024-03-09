from collections import deque, defaultdict
from typing import List

class Solution:
    def bfs(self, beginWord, endWord, wordList, adj):
        queue = deque()
        queue.append((beginWord, 1))
        visited = {beginWord: 1}
        while queue:
            word, level = queue.popleft()
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i+1:]
                    if next_word in wordList:
                        if next_word not in visited:
                            visited[next_word] = level + 1
                            queue.append((next_word, level + 1))
                        if visited[next_word] == level + 1:  # Only shorter or equal paths are allowed
                            adj[word].append(next_word)

    def dfs(self, word, endWord, adj, path, result):
        if word == endWord:
            result.append(path)
            return
        for next_word in adj[word]:
            self.dfs(next_word, endWord, adj, path + [next_word], result)

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList = set(wordList)
        if endWord not in wordList:
            return []
        adj = defaultdict(list)
        self.bfs(beginWord, endWord, wordList, adj)
        result = []
        self.dfs(beginWord, endWord, adj, [beginWord], result)
        return result
