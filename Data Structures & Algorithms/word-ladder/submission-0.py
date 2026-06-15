from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)

        if endWord not in wordSet:
            return 0

        queue = deque()
        queue.append((beginWord, 1))  # (current word, steps so far)
        visited = set()
        visited.add(beginWord)

        while queue:
            word, steps = queue.popleft()

            if word == endWord:
                return steps

            # try changing every position
            for i in range(len(word)):
                # try every letter a-z
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    newWord = word[:i] + c + word[i+1:]

                    if newWord in wordSet and newWord not in visited:
                        visited.add(newWord)
                        queue.append((newWord, steps + 1))

        return 0