#https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=false

x= int(input()) 
y= int(input()) 
z= int(input()) 
n= int(input()) 


ans = []

cordinates = [[i, j, k,] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1)]
for i in cordinates:
    if (i[0] + i[1] + i[2] != n ):
        ans.append(i)
    else:
        continue

print(ans)