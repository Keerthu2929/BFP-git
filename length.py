# length
li = [1,5,1,7,1,3,1,2,1,6]
n = len(li)
ans = 0
for i in range(n):
  if li[i] == 1 :
    ans += 1
print(ans)
