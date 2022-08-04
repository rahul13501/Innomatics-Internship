# Enter your code here. Read input from STDIN. Print output to STDOUT
s= set(input().split())
N = int(input())
output = True

for i in range(N):
    s2 = set(input().split())
    if not s2.issubset(s):
        output = False
    if len(s2) >= len(s):
        output = False

print(output)