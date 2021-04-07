from anytree import NodeMixin

class MyNode(NodeMixin):

  def __init__(self, name, parent=None, id=None, type=None, label=None, children=None):
    super(MyNode, self).__init__()

    self.name = name
    self.type = type
    self.parent = parent
    if children:
      self.children = children

