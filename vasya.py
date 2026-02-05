n ,h = map(int,input().split())
count = n
lst = list(map(int,input().split()))
for d in lst :
    if d > h :
        count += 1
print(count)           