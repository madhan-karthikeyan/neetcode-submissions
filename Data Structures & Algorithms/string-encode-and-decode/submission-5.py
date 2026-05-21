class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == [""]:
            return ""
        if strs == []:
            return "-1"
        return "-azcv+".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "":
            return [""]
        if s == "-1":
            return []
        return s.split("-azcv+")
