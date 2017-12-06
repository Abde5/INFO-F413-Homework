from Treap import Treap

if __name__ == "__main__":
    tree = Treap()
    tree.insert(1)
    tree.insert(3)
    tree.insert(-1)
    tree.insert(4)
    tree.insert(2)

    print(tree)

    print(tree.find(3))
    tree.leftRotation(tree.find(3))

    print(tree)
