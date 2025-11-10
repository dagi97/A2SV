# Problem: A. Beautiful Matrix - https://codeforces.com/problemset/problem/263/A

mat =[]
ind = -1

for i in range(5):
    a = list(map(int, input().split()))
    mat.append(a)

    for j in range(5):
        if mat[i][j]:
            ind = (i,j)
            break
print(abs(ind[0]-2) + abs(ind[1]-2))

    