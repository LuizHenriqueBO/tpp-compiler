from anytree import Node
from anytree.exporter import UniqueDotExporter
root = Node("root")
s0 = Node("programa", parent=root)
s0a = Node("funções", parent=s0)
s0a2 = Node("variável_X", parent=s0a)
s0b2 = Node("variávei_Y", parent=s0a)

# s0a3 = Node("String", parent=s0b2)
# s0a4 = Node("Integer", parent=s0b2)
# s0a5 = Node("Boolean", parent=s0b2)
# s0a6 = Node("Float", parent=s0b2)


# s0b3 = Node("String", parent=s0a2)
# s0b4 = Node("Integer", parent=s0a2)
# s0b5 = Node("Boolean", parent=s0a2)
# s0b6 = Node("Float", parent=s0a2)

UniqueDotExporter(root).to_picture("../imagens/imagens 2/example_tree3.png")