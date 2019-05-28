def longStr(s):
    cont = 0
    prev = 0
    length = 0
    for letter in s:
        if cont%2!=0:
            if letter==")":
                cont+=1
        if letter=="(":
            cont+=1
        prev+=1
        if prev>cont:
            length=cont
            prev = 0
            cont = 0
    return length

print(longStr(")(()())()()()())"))