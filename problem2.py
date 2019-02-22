import sys
class STNode:

    def __init__(self, x: str):
        self.key = x
        self.left = None
        self.right = None


class SyntaxTree:

    def init_helper(self, i: int, l: 'list of strings') -> STNode:
        if i >= len(l):
            return None

        node = STNode(l[i])
        node.left = self.init_helper(2 * i, l)
        node.right = self.init_helper(2 * i + 1, l)
        return node

    def __init__(self, l: 'list of strings') -> 'complete syntax tree':
        self.root = self.init_helper(1, l)

    def inprint(self,x,p):
        if x != None:
            if x.left is None and x.right is None:
                p.append(x.key)
            else:
                p.append('(')
                self.inprint(x.left,p)
                p.append(x.key)
                self.inprint(x.right,p)
                p.append(')')
        return ''.join(p)

    def calculate(self,root):
        if root is None:
            return
        if root.left is None and root.right is None:
            return int(root.key)
        left_sum = self.calculate(root.left)
        right_sum = self.calculate(root.right)
        if root.key == '-':
            return left_sum - right_sum
        elif root.key == '+':
            return left_sum + right_sum
        elif root.key == '/':
            return left_sum / right_sum
        elif root.key == '*':
            return left_sum * right_sum

def driver():
    with open(sys.argv[1]) as f:
        n = int(f.readline().strip())
        in_data = [None]+f.readline().strip().split()
        S = SyntaxTree(in_data)
        p=S.inprint(S.root,[])
        print(p)
        print(S.calculate(S.root))

# this starter code should work with either python or python3
if __name__ == "__main__":
    driver()
