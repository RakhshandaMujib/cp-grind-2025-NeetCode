# Title: Top K Frequent Elements
# Link: https://neetcode.io/problems/top-k-elements
# Difficulty: Medium 
# Tags: Arrays, Hashing

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Get the hash map of the num and its count
        counter = {num : nums.count(num) for num in nums}
        #Create a list of lists of length equal 
        #to the total number of elements in the list
        #The index of this list will be the count
        result = [list() for _ in range(len(nums))]

        #Add num to the bucket of count
        for num, count in counter.items():
            result[count-1].append(num)
        
        #Flatten the result such that everything is in order
        flat_result = [item for sublist in result if isinstance(sublist, list) for item in sublist]
        
        #Return k nums from the end
        return flat_result[-k:]
        