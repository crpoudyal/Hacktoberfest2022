for _ in range(int(input())):
    n,m=map(int,input().split())
    l=[]
    mp={}
    for i in range(n):
        s=input()
        l.append(s)
    for i in l:
        x=''.join(sorted(i))
        if x not in mp:
            mp[x]=1
        else:
            mp[x]=mp[x]+1
    print(len(mp))    
        