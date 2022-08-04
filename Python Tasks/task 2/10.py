n = int(input())
s = set(map(int, input().split()))
num = int(input())
for i in range(num):
    it = input().split()
    if it[0]=="remove":
        s.remove(int(it[1]))
    elif it[0]=="discard":
        s.discard(int(it[1]))
    else :
        s.pop()
print(sum(list(s))) 