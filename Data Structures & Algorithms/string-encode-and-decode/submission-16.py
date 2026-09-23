class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res+= f"{len(s)}#{s}"

        return res

    def decode(self, s: str) -> List[str]:
        num = ""
        i = 0
        res = []
        while i < len(s):
            if s[i].isnumeric():
                num += s[i]
                i += 1
            
            elif s[i] == "#":
                length = int(num)
                num = ""
                res.append(s[i+1:i+1+length])
                i = i + 1 + length

        return res

