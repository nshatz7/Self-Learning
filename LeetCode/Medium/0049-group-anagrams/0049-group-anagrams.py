import json
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        output = {}

        for word in strs:
            key = tuple(sorted(word))
            if key in output:
                output[key].append(word)
            else:
                output.setdefault(key, []).append(word)
            
            output[key].sort()
        
        return list(output.values())


        

        

                
            
                

        
        