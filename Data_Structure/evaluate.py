import operator
def evaluate(parse_tree):
    opers={'+':operator.add,'-':operator.sub,'*':operator.mul,'/':operator.truediv}

    left=parse_tree.get_left_child()
    right=parse_tree.get_right_child()

    if left and right:
        fn=opers[parse_tree.get_root_val()]
        return fn(evaluate(left),evaluate(right))

    else:
        return parse_tree.get_root_val()
