import string
import random

MAX_SIZE_STRING = 100

def random_string(length_of_string):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string))


def random_newick_tree_aux(size):
    if size == 1:
        return random_string(random.randint(1,MAX_SIZE_STRING))  
    else:
        subtree_size = random.randint(1,size-1)
        return '(' + random_newick_tree_aux(subtree_size) + ',' + random_newick_tree_aux(size-subtree_size) + ')'
    
def random_newick_tree(size):
    return random_newick_tree_aux(size) + ';'

