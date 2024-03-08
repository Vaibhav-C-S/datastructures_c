from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        visited = set()
        queue = deque()
        wordList = set(wordList)
        queue.append((beginWord,1))
        visited.add(beginWord)
        start_num = ord('a')
        end_num = ord('z')
        mintime = len(wordList)

        while queue:
            word,time = queue.popleft() 
            if word == endWord:
                return time 
            for i in range(len(word)):
                for j in range(start_num,end_num+1):
                    new_word = word[:i] + chr(j) + word[i+1:]
                    if new_word in wordList and new_word not in visited:
                        queue.append((new_word,time+1))
                        visited.add(new_word)
        return 0


        
        
