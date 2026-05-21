class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        size = left = right = 0
        subStr = ""
        for i in range(len(s)):
            if s[i] not in subStr:
                subStr += s[i]
                right+=1
            else:
                while s[i] in subStr:
                    subStr = subStr[1:]
                    left +=1
                subStr += s[i]
                right += 1
            size = max(size, len(subStr))
        return size