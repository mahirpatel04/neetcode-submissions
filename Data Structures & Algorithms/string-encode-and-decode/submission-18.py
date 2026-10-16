class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += f"{len(s)}#{s}"

        return res

    def decode(self, s: str) -> List[str]:
        length = ""
        res = []
        i = 0
        while i < len(s):
            c = s[i]

            if c.isnumeric():
                length += c
                i += 1
            
            else:
                lengthNumeric = int(length)
                res.append(s[i + 1: i + 1 + lengthNumeric])
                length = ""
                i += 1 + lengthNumeric

        return res

