# logical operators (and, or, and not)
li = [12,3,4,2,18,6]
ans = 0
for i in li:
  if i % 4 == 0 and i % 3 == 0:
    ans += 1
print(ans)

# or

# li = [2,5,9,8,6,24,80]
# ans = 0
# for i in li:
#   if i % 3 == 0 or i % 2 == 0:
#     ans += 1
# print(ans)