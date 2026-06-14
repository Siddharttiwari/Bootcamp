 def preorderTraversal(self, root) :
        arr = []

        def preorder(node):
            if node is None:
                return

            arr.append(node.val)

            preorder(node.left)
            preorder(node.right)

        preorder(root)

        return arr