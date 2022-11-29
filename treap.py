from collections import namedtuple
from random import *

CartNode = namedtuple('CartNode', ['val', 'rand', 'left', 'right', 'nbnodes'])
MAX_RAND = 10**9

def cart_split(tree, v):
	""" Returns a, b : a values < s, b values >= s """
	if tree == None:
		return None, None
	elif tree.val < v:
		a, b = cart_split(tree.right, v)
		if b == None:
			return CartNode(tree.val, tree.rand, tree.left, a, tree.nbnodes), b
		else:
			return CartNode(tree.val, tree.rand, tree.left, a, tree.nbnodes-b.nbnodes), b
	else:
		a, b = cart_split(tree.left, v)
		if a == None:
			return a, CartNode(tree.val, tree.rand, b, tree.right, tree.nbnodes)
		else:
			return a, CartNode(tree.val, tree.rand, b, tree.right, tree.nbnodes-a.nbnodes)

def cart_merge(a, b):
	if a == None or b == None:
		return a or b
	if a.rand >= b.rand:
		return CartNode(a.val, a.rand, a.left, cart_merge(a.right, b), a.nbnodes + b.nbnodes)
	else:
		return CartNode(b.val, b.rand, cart_merge(a, b.left), b.right, a.nbnodes + b.nbnodes)

def cart_tree_expend(a, b):
	if a == None :
		return b
	if b == None:
		return a
	
	return cart_tree_expend(a.left,cart_insert(cart_tree_expend(a.right,b),a.val))

def cart_insert(tree, v):
	a, c = cart_split(tree, v)
	b = CartNode(v, randint(1, MAX_RAND), None, None, 1)
	return cart_merge(cart_merge(a, b), c)

def cart_remove(tree, v):
	a, b = cart_split(tree, v)
	b, c = cart_split(b, v+1)
	return cart_merge(a, c)

def cart_get(tree, v):
	if tree:
		if tree.val == v: return tree
		if tree.val < v: return cart_get(tree.left, v)
		return cart_get(tree.right, v)

def cart_in(tree, v):
	return bool(cart_get(tree, v))

def cart_new_tree(values):
	t = None
	for v in values:
		t = cart_insert(t, v)
	return t

