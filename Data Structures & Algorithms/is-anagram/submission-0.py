class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = {}
        count_t = {}
        for char in s:
            if char in count_s:
                count_s[char] += 1
            else:
                count_s[char] = 1
        for chars in t:
            if chars in count_t:
                count_t[chars] += 1
            else:
                count_t[chars] = 1
        if count_s == count_t:
            return True
        return False                            

        