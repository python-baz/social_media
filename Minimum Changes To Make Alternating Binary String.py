class Solution:
    def cntModify(self, st, chr):
        cnt = 0
        for c in st:
            if c != chr:
                cnt += 1
            chr = '1' if chr == '0' else '0'
        return cnt
        
    def minOperations(self, s: str) -> int:
        res0 = self.cntModify(s, '0')
        res1 = self.cntModify(s, '1')
        return min(res0, res1)