def long(n):
    max=len(n[0])
    for i in n:
        if(len(i)>max):
            max=len(i)
    print('the length',max)
n=[]
m=int(input("enter the number of words: "))
for j in range(0,m):
    i=input()
    n.append(i)
long(n)