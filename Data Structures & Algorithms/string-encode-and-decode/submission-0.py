class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for i in strs:
             encoded_string += str(len(i))+"$"+i

        return encoded_string



    def decode(self, s: str) -> list[str]:
        """Decodes a single string to a list of strings."""
        decoded_strings = []
        i = 0
        
        while i < len(s):

            j = i
            while s[j] != "$":
                j += 1

            length = int(s[i:j])
            
            word = s[j + 1 : j + 1 + length]
            decoded_strings.append(word)

            i = j + 1 + length
            
        return decoded_strings