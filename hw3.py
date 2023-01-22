import time
from typing import List


# ==== Part 1 =====
def memorize_3s(func):
    cache = {}
    def f(x):
        curr_time = time.time()
        if x in cache and curr_time - cache[x] < 3:
            cache[x] = curr_time
            return x
        else:
            cache[x] = curr_time
            return func(x)
    return f


@memorize_3s
def identity(x):
    print('this function is called')
    return x
  
  
identity(1) # there should be a print
identity(1) # there should no print

time.sleep(3)
identity(1) # there should be a print



# ==== Part 2 =====

# this is the definition of the binary tree
class Node:
    def __init__(self, key, left=None, right=None):
        self.left = left
        self.right = right
        self.val = key
        
        
        
# this is saying that the function takes one argument, which is type = Node
# and returns a list of string
def pre_order_recursion(root: Node) -> List[str]:
    result = []
    if root:
        result.append(root.val)
        result.extend(pre_order_recursion(root.left))
        result.extend(pre_order_recursion(root.right))
    return result

def pre_order_iteration(root: Node) -> List[str]:
    stack = [root]
    result = []
    while stack:
        node = stack.pop()
        if node:
            result.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
    return result


def in_order_recursion(root: Node) -> List[str]:
    result = []
    if root:
        result.extend(in_order_recursion(root.left))
        result.extend([root.val])
        result.extend(in_order_recursion(root.right))
    return result

def in_order_iteration(root: Node) -> List[str]:
    stack = []
    result = []
    node = root
    while True:
        if node:
            stack.append(node)
            node = node.left
        elif stack:
            node = stack.pop()
            result.append(node.val)
            node = node.right
        else:
            break
    return result

def post_order_recursion(root: Node) -> List[str]:
    result = []
    if root:
        result.extend(post_order_recursion(root.left))
        result.extend(post_order_recursion(root.right))
        result.append(root.val)
    return result

def post_order_iteration(root: Node) -> List[str]:
    result = []
    stack1 = [root]
    stack2 = []
    if root:
        while stack1:
            node = stack1.pop()
            stack2.append(node)
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
        while stack2:
            node = stack2.pop()
            result.append(node.val)
    return result

  
  
  # ====== test case below ======
# this is the initiation of the testing object.
# DO NOT MODIFY THIS
root = Node('F', 
    left=Node(
        'B',
        left=Node('A'),
        right=Node('D', left=Node('C'), right=Node('E')),
    ), 
    right=Node('G', right=Node('I', left=Node('H')))
)


assert pre_order_recursion(root) == pre_order_iteration(root) == ['F', 'B', 'A', 'D', 'C', 'E', 'G', 'I', 'H']
assert in_order_recursion(root) == in_order_iteration(root) == ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
assert post_order_recursion(root) == post_order_iteration(root) == ['A', 'C', 'E', 'D', 'B', 'H', 'I', 'G', 'F']
