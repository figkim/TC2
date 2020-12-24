class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_dict = {}
        
        for word in strs:
            ord_word = tuple(sorted(word))
            
            if ord_word not in ana_dict:
                ana_dict[ord_word] = [word]
            else:
                ana_dict[ord_word].append(word)
                
        return ana_dict.values()
