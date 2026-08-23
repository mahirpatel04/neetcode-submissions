class Solution:
    def compress(self, chars: List[str]) -> int:
        w = 0
        r = 0
        count = 0
        while r < len(chars):
            # print(chars)
            chars[w] = chars[r]
            count += 1

            e = r + 1
            while e < len(chars) and chars[e] == chars[r]:
                e += 1

            if e - r != 1:
                for c in str(e-r):
                    w += 1
                    chars[w] = c

                    count += 1
            
            r = e
            w += 1


        return count