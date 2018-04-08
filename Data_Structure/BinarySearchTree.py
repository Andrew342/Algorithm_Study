# Basic BinarySearchTree class - incomplete

class BinarySearchTree:
    def __init__(self):
        self.root=None
        self.size=0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def put(self,key,val):
        if self.root:
            self._put(key,val,self.root)
        else:
            self.root=TreeNode(key,val)
        self.size=self.size+1

    def _put(self.key,val,current_node):
        if key<current_node.key:
            if current_node.has_left_child():
                self._put(key,val,current_node.left_child)
            else:
                current_node.left_child=TreeNode(key,val,parent=current_node)
        else:
            if current_node.has_right_child():
                self._put(key,val,current_node.right_child)
            else:
                current_node.right_child=TreeNode(key,val,parrent=current_node)

    def __setitem__(self,k,v):
        self.put(k,v)

    def get(self,key):
        if self.root:
            res=self._get(key,self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            None

    def _get(self,key,current_node):
        if not current_noe:
            return None
        elif current_noe.key==key:
            return current_node
        elif key<current_node.key:
            return self._get(key,current_node.left_child)
        else:
            return self._get(key,current_node.right_child)

    def __getitem__(self.key):
        return self.get(key)

    def __contains__(self,key):
        if self._get(key,self.root):
            return True
        else:
            False

    def delete(self,key):
        if self.size>1:
            node_to_remove=self._get(key,self.root)
            if node_to_remove:
                self.remove(node_to_remove)
                self.size=self.size-1
            else:
                raise KeyError('Error,key not in tree')
        elif self.size==1 and self.root.key==key:
            self.root=None
            self.size=self.size-1
        else:
            raise KeyError('Error,key not in tree')

    def __delitem__(self.key):
        self.delete(key)
