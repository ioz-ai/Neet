# In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

# Given a sequence of words written in the alien language, and the order of the alphabets, return true if and only if the given words are sorted lexicographically in this alien language.

class Solution:
    order_map = {}

    def fillIn(self, order: str):
        for i, char in enumerate(order):
            self.order_map[char] = i 

    def lessThan(self, str1: str, str2:str) ->bool:
        len1, len2 = len(str1), len(str2)

        for i in range(min(len1, len2)):
            rank1 = self.order_map[str1[i]]
            rank2 = self.order_map[str2[i]]
            
            if rank1 != rank2:
                return rank1 < rank2

        if len(str2) < len(str1):
            return False

        return True

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        self.fillIn(order)

        for i in range(1, len(words)):
            if not self.lessThan(words[i-1], words[i]):
                return False
            
        return True
