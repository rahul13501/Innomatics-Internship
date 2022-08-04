# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())

for _ in range(T):
    a = int(input())
    A = set(input().split())
    b = int(input())
    B = set(input().split())
    print(A.issubset(B))