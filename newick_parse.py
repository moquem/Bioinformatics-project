from collections import namedtuple

Node = namedtuple('Node', ['val','left','right'])

def stringToNewick(s):
    if s[-1] == ';':
        s = s[:len(s)-1]
    if s[0] != '(':
        return Node(s,None,None)
    s = s[1:len(s)-1]
    parenthese = 0
    fils = False
    i = 0
    while parenthese > 0 or not(fils):
        if s[i] == "(":
            parenthese += 1
            i += 1
        elif s[i] == ")":
            parenthese -= 1
            i += 1
        elif parenthese == 0 and s[i] == ",":
            fils = True
        else:
            i += 1
    return Node(None,stringToNewick(s[:i]),stringToNewick(s[i+1:]))

def newickToString_aux(T):
    if T.val != None:
        return T.val
    else:
        s1 = newickToString_aux(T.left)
        s2 = newickToString_aux(T.right)
        return ('('+s1+','+s2+')')

def newickToString(T):
    return newickToString_aux(T) + ';'