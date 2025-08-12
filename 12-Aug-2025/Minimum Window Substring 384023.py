# Problem: Minimum Window Substring - https://leetcode.com/problems/minimum-window-substring/submissions/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
 
        mydict_t = Counter(t)
        required = len(mydict_t)
        window_dict = defaultdict(int)
        acquired = 0
        n = len(s)
        solution = (-1,n+1)
        left = 0
        
        for right in range (n):
            char = s[right]
            window_dict[char] += 1
            if char in mydict_t:
                if window_dict[char] == mydict_t[char]:
                    acquired += 1
            while acquired == required:
                lchar = s[left]
                if solution[1] - solution[0] > right - left:
                    solution = (left,right)
                window_dict[lchar] -= 1

                if lchar in mydict_t:
                    if window_dict[lchar] < mydict_t[lchar]:
                        acquired -= 1
                left += 1
        if solution[0] == -1:
            return ''
        else:
            return s[solution[0]:solution[1]+1]


                