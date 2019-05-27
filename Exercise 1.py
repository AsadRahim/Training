from itertools import permutations
def strProg(words,s):
    output = list()
    wordLen = len(words[0])
    wordsLen = len(words)
    wordsPermutaions = ["".join(map(str, perm)) for perm in permutations(words, wordsLen)]
    for perms in wordsPermutaions:
        nex = len(perms)
        curr = 0
        cont = 0
        for i in range(0,len(s)):
           b=s[curr:nex]
           if(b==perms):
                 cont=1
           if(cont==1):
                 ind = nex-(wordsLen*wordLen)
                 output.append(ind)
                 cont=0
           curr += 1
           nex += 1
           if(nex>=len(s)):
               nex=len(s)
    return output

s="barefoofooebarbarefooetc"
words=["bar","foo"]
print (strProg(words,s))
