try:
    import lxml
    from lxml import etree
except ImportError as e:
    print e.message

from PIA.Rockwell.XML.Tools import *
from Base_Template import Base_Template

class Rung(Base_Template):
    '''
    Rung Template:
    See L5X Manual for Details,
    These members are to be used when defining a ladder rung.
    ----------------------------------------------------------
    For Information on this see the provided L5X Manual from Rockwell
    '''
    def __init__(self, Number, Comment = "", Content = "NOP();"):
            #Initialize Member Attributes
            self.root = etree.Element("Rung")
            self.root.set("Number", str(Number))
            self.root.set("Type", "N")
            if Comment != "":
                self.Comment = etree.SubElement(self.root, 'Comment')
                self.setComment(Comment)
                self.root.append(self.Comment)

            self.rungContent = etree.SubElement(self.root, "Text")
            self.setRungContent(Content)

    def setRungContent(self, Content):
        assert type(Content) == str
        self.rungContent.text = etree.CDATA(Content)

    def setComment(self, Comment):
        assert type(Comment) == str
        if self.Comment == None:
            self.Comment = etree.SubElement(self.root, 'Comment')
            self.root.append(self.Comment)
        self.Comment.text = etree.CDATA(Comment)

    def setParent(self, parent):
        assert etree.iselement(parent) and parent.tag == "RLLContent"
        parent.append(self.root)
