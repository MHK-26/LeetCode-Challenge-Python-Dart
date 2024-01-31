class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create a dictionary to store the frequency of each number
        hashMap = {}
        
        # Count the frequency of each number in the list
        for num in nums:
            if num in hashMap:
                hashMap[num] += 1
            else:
                hashMap[num] = 1

        # Sort the dictionary by values in descending order, and get the first k keys by using [:k]
        top_k = sorted(hashMap, key=hashMap.get, reverse=True)[:k]
        
        return top_k
