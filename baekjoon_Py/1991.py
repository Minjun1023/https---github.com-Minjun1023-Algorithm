import sys
input = sys.stdin.readline
n = int(input())
tree = {}
for i in range(n):
    root, left, right = input().split()
    tree[root] = [left, right]

# root -> left -> right 순서
def preorder(root):
    if root != '.':
        print(root, end='') # root
        preorder(tree[root][0]) # left
        preorder(tree[root][1]) # right
# left -> root -> right 순서
def inorder(root):
    if root != '.':
        inorder(tree[root][0]) # left
        print(root, end='') # root
        inorder(tree[root][1]) # right
# left -> right -> root 순서
def postorder(root):
    if root != '.':
        postorder(tree[root][0]) # left
        postorder(tree[root][1]) # right
        print(root, end='') # root

# 노드의 이름은 A부터 시작이므로
preorder('A')
print()
inorder('A')
print()
postorder('A')
