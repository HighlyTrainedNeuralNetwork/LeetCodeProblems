class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def printTree(root):
    def height(root):
        if root is None:
            return -1
        return 1 + max(height(root.left), height(root.right))
    def populate(root, matrix, r, c):
        if root:
            matrix[r][c] = str(root.val)
            if root.left:
                populate(root.left, matrix, r + 1, c - 2 ** (height - r - 1))
            if root.right:
                populate(root.right, matrix, r + 1, c + 2 ** (height - r - 1))

    height = height(root)
    width = 2 ** (height + 1) - 1
    matrix = [[""] * width for i in range(height + 1)]
    populate(root, matrix, 0, (width - 1) // 2)
    print(matrix)

root = TreeNode(val=1)
root.left = TreeNode(val=2)
root.right = TreeNode(val=3)
root.right.right = TreeNode(val=4)


printTree(root)