# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
a=set(map(int, input().split()))
m=int(input())
b=set(map(int, input().split()))
c=a.difference(b)
d=b.difference(a)
e=c.union(d)
for i in sorted(list(e)):
    print(i)