try:
    import lxml
    from lxml import etree
except ImportError as e:
    print e.message

from PIA.Rockwell.XML.Tools import *
from Base_Template import Base_Template

class TagComment(Base_Template):
    '''
    Tag Comment Template:
    See L5X Manual for Details,
    These members are to be used when defining a tag's comment.
    ----------------------------------------------------------
    [specifier].[BitNumber]
    ----------------------------------------------------------
    For Information on this see the provided L5X Manual from Rockwell
    '''
    def __init__(self, Description):
            #Initialize Member Attributes
            self.root = etree.Element("Comment")
            self.root.set("Operand", "Specifier")
            setDescription(Description)
            self.setDescription(Description)

    def setDescription(self, Description):
        assert type(Description) == str
        self.root.text = etree.CDATA(Description)

    def setParent(self, parent):
        assert etree.iselement(parent) and parent.tag == "Comments"
        parent.append(self.getLocalRoot())

    def getLocalRoot(self):
        return self.root

    def __str__(self):
        return etree.tostring(self.root, pretty_print = True)
