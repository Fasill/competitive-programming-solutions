class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create an empty dictionary to store anagrams
        anagrams = {}

        # Iterate through the input list of strings
        for word in strs:
            # Sort the characters in the current word and join them back together
            sorted_word = "".join(sorted(word))
            
            # Check if the sorted word is already in the dictionary
            if sorted_word not in anagrams:
                # If not, create a new entry with the sorted word as the key
                # and a list containing the current word as the value
                anagrams[sorted_word] = [word]
            else:
                # If the sorted word is already in the dictionary,
                # append the current word to the list of anagrams
                anagrams[sorted_word].append(word)

        # Extract the values (lists of anagrams) from the dictionary
        x = [i for i in anagrams.values()]
        
        return x
