class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1 = list(s)
        l2 = list(t)
        d1 = dict()
        d2 = dict()
        for i in l1:
            if i not in d1:
                d1[i] = l1.count(i)
        
        for i in l2:
            if i not in d2:
                d2[i] = l2.count(i)

        print(d1)
        print(d2)

        return True if d1==d2 else False