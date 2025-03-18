# Problem: C - Penalty Shootout - https://codeforces.com/gym/596141/problem/C

from math import ceil
for _ in range(int(input())):
    s = input()
    one, two = 0,0
    m_one , m_two = 0, 0
    flag = True 
    for i in range(10):
        remain = 10 - i
        if i%2:
            if one + remain//2 < two + m_two or two + ceil(remain/2) < one + m_one:
                print(i)
                flag = False
                break
            if s[i] == '1':
                two += 1
            elif s[i] == '?':
                m_two += 1
        
        else:
            if one + ceil(remain/2) < two + m_two or two+ remain//2 < one + m_one:
                print(i)
                flag = False
                break
            if s[i] == '1':
                one += 1
            elif s[i] == '?':
                m_one += 1

    if flag:
        print(10)
                


   
        
