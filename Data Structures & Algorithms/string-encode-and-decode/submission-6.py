class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += f"{len(s)}#{s}"

        return res

    def decode(self, s: str) -> List[str]:
        num = ""
        res = []
        i = 0
        while i < len(s):
            if s[i].isnumeric():
                num += s[i]
                i += 1
            
            elif s[i] == "#":
                res.append(s[i + 1 : i + 1 + int(num)])
                i += int(num) + 1

                num = ""

        return res
