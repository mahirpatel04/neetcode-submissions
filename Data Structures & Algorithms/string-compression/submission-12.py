class Solution:
    def compress(self, chars: List[str]) -> int:
        w = 0
        r = 0
        count = 0
        while r < len(chars):
            # Immediately write the new unique segment identifier
            chars[w] = chars[r]

            # Increase count of compressed string
            # Set the current writer pointer to the next splot
            count += 1
            w += 1

            # Calculate how far this segment can be extended:
            e = r + 1
            # Keep extended until they are equal. Eventually we will have gone up until first element that doesn't match what we just read
            while e < len(chars) and chars[e] == chars[r]:
                e += 1

            # If the difference is greater than 1 then we also need to add the length for each of the characters in the string version put it in and shift the writing pointer one over while also maintaining a count
            if e - r != 1:
                for c in str(e-r):
                    chars[w] = c
                    w += 1
                    count += 1
            
            r = e
            


        return count