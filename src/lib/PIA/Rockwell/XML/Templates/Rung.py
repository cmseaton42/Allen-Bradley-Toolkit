try:
    import lxml
    from lxml import etree
except ImportError as e:
    print e.message

from lib.PIA.Rockwell.XML.Tools import *

class Rung():
    '''
    Rung Template:
    See L5X Manual for Details,
    These members are to be used when defining a datatype.
    ----------------------------------------------------------
    For Information on this see the provided L5X Manual from Rockwell
    '''
    def __init__(self, Number, Comment = "", Content = "NOP();"):
            #Initialize Member Attributes
            assert isValidTag(TypeName)
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

    def setAttribute(self, **kwargs):
        for key in kwargs:
            if not key in self.root.keys():
                raise KeyError("Rung has No Attribute: <%s>" % key)

        for key in kwargs:
            self.root.set(key, kwargs[key])

    def setComment(self, Comment):
        assert type(Comment) == str
        if self.Comment == None:
            self.Comment = etree.SubElement(self.root, 'Comment')
            self.root.append(self.Comment)
        self.Comment.text = etree.CDATA(Comment)

    def setParent(self, parent):
        assert etree.iselement(root) and root.tag == "RLLContent"
        root.append(self.root)

    def getLocalRoot(self):
        return self.root

    def __str__(self):
        return etree.tostring(self.root, pretty_print = True)
