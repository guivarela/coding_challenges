# coding_challenges
some coding problems solved
t = int(input())
for x in range(t):
    n = int(input())       
    s = [int(i) for i in input().split()]
    s = sorted(s)
    re = s[1]-s[0]
    for z in range(n-1):
        aux = s[z+1]-s[z]
        re = min(aux, re)
    print(re)
