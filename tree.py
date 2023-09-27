#Author - Sachin Jain
#Date - 14 th May, 2023
#File - tree.py
#Description- it converts postfix to exptree, and evaluates it!

from stack import Stack

class BinaryTree:
    def __init__(self,rootObj=None):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key

    def __str__(self):
        s = f"{self.key}"
        s += '('
        if self.leftChild != None:
            s += str(self.leftChild)
        s += ')('
        if self.rightChild != None:
            s += str(self.rightChild)
        s += ')'
        return s

class ExpTree(BinaryTree):

    def make_tree(postfix):
        stack = Stack()
        for maverick in postfix:
            if maverick.isdigit() or '.' in maverick:
                stack.push(ExpTree(maverick))
            elif maverick in '+-*/^':
                rightwing = stack.pop()
                leftwing = stack.pop()
                newbie = ExpTree(maverick)
                newbie.leftChild = leftwing
                newbie.rightChild = rightwing
                stack.push(newbie)
        return stack.pop()

    def preorder(tree):
        s = ''
        if tree is not None:
            s = tree.getRootVal()
            s += ExpTree.preorder(tree.getLeftChild())
            s += ExpTree.preorder(tree.getRightChild())
        return s

    def inorder(tree):
        s = ''
        if tree is not None:
            if tree.getLeftChild() is not None:
                s += '(' + ExpTree.inorder(tree.getLeftChild())
            s += str(tree.getRootVal())
            if tree.getRightChild() is not None:
                s += ExpTree.inorder(tree.getRightChild()) + ')'
        return s

    def postorder(tree):
        s = ''
        if tree is not None:
            s += ExpTree.postorder(tree.getLeftChild())
            s += ExpTree.postorder(tree.getRightChild())
            s += tree.getRootVal()
        return s

    def evaluate(tree):
        if tree == None:
            return None
        if tree.getLeftChild() == None and tree.getRightChild() == None:
            return float(tree.getRootVal())
        righty = ExpTree.evaluate(tree.getRightChild())
        lefty = ExpTree.evaluate(tree.getLeftChild())
        if tree.getRootVal() == '-':
            return lefty - righty
        elif tree.getRootVal() == '+':
            return lefty + righty
        elif tree.getRootVal() == '^':
            return lefty ** righty
        elif tree.getRootVal() == '/':
            return lefty / righty
        elif tree.getRootVal() == '*':
            return lefty * righty
        else:
            return float(tree.getRootVal())

    def __str__(self):
        return ExpTree.inorder(self)

# a driver for testing BinaryTree and ExpTree
if __name__ == '__main__':

    # test a BinaryTree

    r = BinaryTree('a')
    assert r.getRootVal() == 'a'
    assert r.getLeftChild()== None
    assert r.getRightChild()== None
    assert str(r) == 'a()()'

    r.insertLeft('b')
    assert r.getLeftChild().getRootVal() == 'b'
    assert str(r) == 'a(b()())()'

    r.insertRight('c')
    assert r.getRightChild().getRootVal() == 'c'
    assert str(r) == 'a(b()())(c()())'

    r.getLeftChild().insertLeft('d')
    r.getLeftChild().insertRight('e')
    r.getRightChild().insertLeft('f')
    assert str(r) == 'a(b(d()())(e()()))(c(f()())())'

    assert str(r.getRightChild()) == 'c(f()())()'
    assert r.getRightChild().getLeftChild().getRootVal() == 'f'


    # test an ExpTree

    postfix = '5 2 3 * +'.split()
    tree = ExpTree.make_tree(postfix)

    assert str(tree) == '(5+(2*3))'
    assert ExpTree.inorder(tree) == '(5+(2*3))'
    assert ExpTree.postorder(tree) == '523*+'
    assert ExpTree.preorder(tree) == '+5*23'
    assert ExpTree.evaluate(tree) == 11.0

    postfix = '5 2 + 3 *'.split()
    tree = ExpTree.make_tree(postfix)
    assert str(tree) == '((5+2)*3)'
    assert ExpTree.inorder(tree) == '((5+2)*3)'
    assert ExpTree.postorder(tree) == '52+3*'
    assert ExpTree.preorder(tree) == '*+523'
    assert ExpTree.evaluate(tree) == 21.0