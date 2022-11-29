import treap
from newick_parse import *
from collections import namedtuple

Node = namedtuple('Node', ['val','left','right'])
get_nbnodes = lambda bt: 0 if bt is None else bt.nbnodes

def numberCrossing(T):
    if T.val != None:
        return 0, treap.cart_new_tree([T.val]),T
    else:
        ncl, btl, Tl = numberCrossing(T.left)
        ncr, btr, Tr = numberCrossing(T.right)
        swap = False
        if btl.nbnodes <= btr.nbnodes:
            value_1 = total_cr(btl,btr)
            value_2 = btl.nbnodes * btr.nbnodes - value_1
            if value_1 > value_2: 
                swap = True
        else:
            value_1 = total_cr(btr,btl)
            value_2 = btl.nbnodes * btr.nbnodes - value_1
            if value_1 < value_2: 
                swap = True
        if swap:
            T = Node(T.val,Tr,Tl)
        else:
            T = Node(T.val,Tl,Tr)

        if get_nbnodes(btl) > get_nbnodes(btr):
            bt = treap.cart_tree_expend(btr,btl)
        else:
            bt = treap.cart_tree_expend(btl,btr)
        nc = ncl+ncr+min(value_1,value_2)
        return nc,bt,T


def cr(v,bt):
    if bt == None:
        return 0
    elif v < bt.val:
        return cr(v,bt.left)
    elif v == bt.val:
        return get_nbnodes(bt.left)
    else:
        return get_nbnodes(bt.left) + 1 + cr(v,bt.right)


def total_cr(btl, btr):
    if btl == None:
        return 0
    else:
        return cr(btl.val,btr) + total_cr(btl.left,btr) + total_cr(btl.right,btr)

def OTCM(s):
    T = stringToNewick(s)
    m,_,newT = numberCrossing(T)
    return m, newickToString(newT)

