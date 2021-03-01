def traverse_bst(root, value):
    if root is None:
        return None
    elif root._value == value:
        return root
    elif value > root:
        return traverse_bst(root._right, value)
    else:
        return traverse_bst(root._left, value)