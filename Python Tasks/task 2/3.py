if __name__ == '__main__':
    lst1=[]
    for _ in range(int(input())):
        name=input()
        score=float(input())
        lst1.append([score,name])
    lst2=sorted(lst1)
    temp=lst2[0][0]
for i in range(len(lst2)):
    if lst2[i][0]>temp:
        seclast=lst2[i][0]
        break
for i in range(len(lst2)):
    if lst2[i][0]==seclast:
        print(lst2[i][1])