class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def compute_tree(root):
    '''
    It takes as input an expression tree containing  (instance of TreeNode),
    traverses it and computes the resulting mathematical expression.
    This expression tree supports the arithmetic operations: +, -, *, /, ^, %.
    @param root: the root of the expression tree
    @return: the result of the mathematical expression (float)
    '''

    if root is None:
        return 0
    if root.left is None and root.right is None:
        return root.val
    left_sum = compute_tree(root.left)
    right_sum = compute_tree(root.right)
    if root.val == '+':
        return left_sum + right_sum
    elif root.val == '-':
        return left_sum - right_sum
    elif root.val == '*':
        return left_sum * right_sum
    