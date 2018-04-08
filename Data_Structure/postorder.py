# import BinaryTree

def postorder(tree):
    if tree:
        postprder(tree.get_left_child())
        postprder(tree.get_right_child())
        print(tree.get_root_val())
