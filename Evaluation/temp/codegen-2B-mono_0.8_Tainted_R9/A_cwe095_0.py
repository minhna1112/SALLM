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

    # code here
    if root is None:
        return 0
    elif root.left is None and root.right is None:
        return root.val
    else:
        if root.val == "+":
            if root.left.val == 0:
                return root.left.val + root.right.val
            else:
                left_sum = compute_tree(root.left)
                right_sum = compute_tree(root.right)
                return left_sum + right_sum
        elif root.