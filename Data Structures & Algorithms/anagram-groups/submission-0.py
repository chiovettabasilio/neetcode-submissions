class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Character zaehlen und groupen in HashMap
        result = defaultdict(list)
        for str in strs:
            anzahl = [0] * 26 #a-z

            for char in str:
                anzahl[ord(char) - ord("a")] += 1   #asci char - asci a , BSP a - a = 0. c - a = 2 -> pos in anzahl der Buchstaben -> an der stelle char um 1 erhoehen

            result[tuple(anzahl)].append(str)
        return list(result.values()) 


