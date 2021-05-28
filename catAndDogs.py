try:
    t=int(input())
    for _ in range(t):
        c,d,l=map(int,input().split())
        max=(c+d)*4
        min=d*4
        if c>2*d:
            min=max-2*min
        if l>max or l<min or l%4!=0:
            print("no")
        else:
            print("yes")
except:
    pass