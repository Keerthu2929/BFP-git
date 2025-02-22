# rev
li = "munibooshanam"
ans = ""
for i in range(12,-1,-1):
    ans = ans + li[i]
print(ans)


# palindrome
li = "level"
ans = ""
for i in range(4,-1,-1):
    ans = ans + li[i]
if ans == li:
    print("Yes")
else:
    print("No")



#### boolean using in palindrome
s = "abcdef"
n = len(s)//2
mu = len(n) 
valid = True
for i in range(n):
    l = s[i]
    r = s[mu - 1 - i]
    if l != r:
        valid = False
if valid:
    print("Yes")
else:
    print("No")


#### boolean using in palindrome and break stat also
s ="amma"
n = len(s)//2
mu = n * 2
valid = True
for i in range(int(n)):
    l = s[i]
    r = s[mu - 1 - i]
    if l != r:
        valid = False
        break
if valid:
    print("Yes")
else:
    print("No")