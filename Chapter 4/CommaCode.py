l = [*map(str,input().split())]
s = ''
for i in range(len(l)):
    if i == (len(l)-1):
        s += 'and '
        s += l[i]
    else :
        s += l[i]
        s += ', '
print(s)