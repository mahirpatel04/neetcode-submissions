class Solution:
    def compress(self, chars: List[str]) -> int:
        curr = chars[0]
        count = 1
        res = ""
        for c in chars[1:]:
            if c == curr:
                count += 1

            else:
                if count != 1:
                    res += f"{curr}{count}"
                else:
                    res += curr

                curr = c
                count = 1
            
        if count != 1:
            res += f"{curr}{count}"
        else:
            res += curr

        for i, c in enumerate(res):
            chars[i] = c

        print(chars)
        return len(res)