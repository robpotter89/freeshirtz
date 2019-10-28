import Levenshtein


class Node(object):
    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent
        self._edges = []

    def __repr__(self):
        return self.data

    @property
    def edges(self):
        return self._edges

    @edges.setter
    def edges(self, node_tuple):
        self._edges.append(node_tuple)

    @property
    def weights(self):
        return [e[0] for e in self._edges]


class BKTree:
    def __init__(self):
        with open('/usr/share/dict/words') as f:
            words = [w.replace('\n', '') for w in f.readlines() if w != 'tshirt']

        self.root = Node('tshirt')
        self.nodes = {'tshirt': self.root}

        for i, word in enumerate(words):
            node_to_check = self.root
            while node_to_check:
                lev = Levenshtein.distance(node_to_check.data, word)
                if lev not in node_to_check.weights:
                    new_node = Node(word, node_to_check)
                    node_to_check._edges.append((lev, new_node))
                    self.nodes[word] = new_node
                    node_to_check = None
                else:
                    edge = [e for e in node_to_check.edges if e[0] == lev][0]
                    node_to_check = edge[1]

    def find_words(self, search):
        node = self.nodes.get(search, None)
        if not node:
            return
        path = []
        while node:
            path.append(node.data)
            node = node.parent

        return path
