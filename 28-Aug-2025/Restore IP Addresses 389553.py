# Problem: Restore IP Addresses - https://leetcode.com/problems/restore-ip-addresses/

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def isvalid(x):
            return 0 <= int(x) <= 255 and (x == '0' or x[0] != '0')
        def backtrack(c  , path):
            if len(path) == 4:
                if c == len(s):
                    res.append('.'.join(path))
            for i in range(1,4):
                if c + i <= len(s):
                    part = s[c:c + i]
                    if isvalid(part):
                        backtrack(c + i, path + [part])
        res = []
        backtrack(0, [])
        return res
        