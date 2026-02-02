class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Remove leading and trailing spaces
        s = s.strip()
        
        # Split by spaces
        words = s.split()
        
        # Return length of the last word
        return len(words[-1])
