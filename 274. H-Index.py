class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse = True)
        n = 0
        while n < len(citations) and citations[n] > n:
            n += 1
        return n
    
