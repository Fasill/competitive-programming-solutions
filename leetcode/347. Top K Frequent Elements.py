class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create a dictionary to store the frequency of each number
        frequency = {}
        
        # Count the frequency of each number in the input list
        for number in nums:
            if number in frequency:
                frequency[number] += 1
            else:
                frequency[number] = 1
        
        # Sort the dictionary by the frequency values in ascending order
        sorted_frequency = sorted(frequency.items(), key=lambda item: item[1])
        
        # Get the top k frequent numbers from the sorted list and convert them to a list
        top_k_frequent = [i for i, _ in sorted_frequency[-k:]]
        
        return top_k_frequent
