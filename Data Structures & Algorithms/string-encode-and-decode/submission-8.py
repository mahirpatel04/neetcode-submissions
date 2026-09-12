class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += f"{len(s)}#{s}"

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        num = ""
        i = 0
        while i < len(s):
            c = s[i]
            if c.isnumeric():
                num += c
                i += 1

            elif c == "#":
                length = int(num)
                num = ""
                word = s[i + 1: i + 1 + length]
                res.append(word)
                i += 1 + length

        return res

