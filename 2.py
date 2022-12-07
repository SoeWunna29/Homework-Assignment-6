class Tree:
    def __init__(self, label, branches=[]):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

    def __repr__(self):
        if self.branches:
            return 'Tree({0}, {1})'.format(self.label, repr(self.branches))
        else:
            return 'Tree({0})'.format(repr(self.label))

    def elements(self):
        lines = []
        for b in self.branches:
            for line in b.elements():
                lines.append(line)
        return [self.label] + lines

    def is_leaf(self):
        return not self.branches

    def average(self):
        list = self.elements()
        sum = 0
        for i in list:
            sum += i
        return sum / len(list)


def ave(t):
    print(t.elements())
    print(t.average())


ave(Tree(11, [Tree(12), Tree(13, [Tree(14), Tree(15)])]))
