
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a dictionary to store anagrams
        hashMap = {}
        
        # Iterate through the list of strings
        for i in range(len(strs)):
            # Sort the characters in the string and join them back
            ssorted = ''.join(sorted(strs[i]))

            # Check if the sorted string is already in the dictionary
            if ssorted in hashMap:
                # If yes, add the original string to the corresponding list
                hashMap[ssorted].append(strs[i])
            else:
                # If not, create a new list and add the original string to it
                hashMap[ssorted] = [strs[i]]
                
        # Convert the values (lists of anagrams) to a list and return
        return list(hashMap.values())
