class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        words1 = sentence1.split()
        words2 = sentence2.split()
        
        # Make sure words1 is always the longer or equal one
        if len(words1) < len(words2):
            words1, words2 = words2, words1
        
        # Start comparing from the beginning
        i = 0
        while i < len(words2) and words1[i] == words2[i]:
            i += 1
        
        # Start comparing from the end
        j = 0
        while j < len(words2) and words1[len(words1) - 1 - j] == words2[len(words2) - 1 - j]:
            j += 1
        
        # The total number of matched words from the beginning and end
        return i + j >= len(words2)
