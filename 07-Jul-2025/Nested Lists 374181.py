# Problem: Nested Lists - https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

if __name__ == '__main__':
    record = []
    check = set()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        record.append([ name ,score])
        check.add(score)
    check = list(check)
    check.sort()
    record = sorted(record , key = lambda x : x[1])
    
    ans = []
    for v,k in record:
        if k == check[1]:
            ans.append(v)
        elif k > check[1]:
            break
    ans.sort()
    for i in ans:
        print(i)
    
        
    