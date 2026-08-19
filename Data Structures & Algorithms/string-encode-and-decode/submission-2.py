class Solution:

    def encode(self, strs: List[str]) -> str:
        code = ""

        for s in strs:
            code += f"{len(s)}.{s}"

        return code

    def decode(self, s: str) -> List[str]:
        num = ""
        strings = []
        i = 0
        while i < len(s):
            if s[i] == ".":
                num = int(num)
                strings.append(s[i+1:i+1+num])
                i += 1 + num
                num = ""

            else:
                num += s[i]
                i += 1

        return strings




