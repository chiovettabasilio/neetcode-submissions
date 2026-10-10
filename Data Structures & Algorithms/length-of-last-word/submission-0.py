class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        end = len(s) - 1 

        #Leerzeichen am Ende überspringen
        while end >= 0 and s[end] == " ":
            end -= 1
        
        #länge berechnen
        length = 0
        while end >= 0 and s[end] != " ":
            length += 1
            end -= 1
        
        return length