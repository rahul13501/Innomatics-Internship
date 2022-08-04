# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
a=set(input().split())
b=int(input())
m=set(input().split())
c=a.union(m)
print(len(c))