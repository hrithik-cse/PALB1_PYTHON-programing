class Solution:
    def lengthOfLastWord(self, s):
        s = s.strip()  # remove extra spaces
        return len(s.split()[-1])
