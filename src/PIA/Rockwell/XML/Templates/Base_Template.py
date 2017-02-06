try:
    import lxml
    from lxml import etree
except ImportError as e:
    print e.message

import os
from PIA.Rockwell.XML.Tools import *

class Base_Template():
    '''
    Base Template Template:
    See L5X Manual for Details,
    USED FOR INHERITANCE ONLY
    ----------------------------------------------------------
    For Information on this see the provided L5X Manual from Rockwell
    '''
    def __init__(self):
            #Initialize Member Attributes
            self.root = None

    def checkIfChild(self, nodeTag):
        assert type(nodeTag) == str
        for node in self.root:
            if node.tag == nodeTag: return True
        return False

    def setAttribute(self, kwargs):
        for key in kwargs:
            if not key in self.root.keys():
                raise KeyError("%s has No Attribute: <%s>" % (self.root.tag, key))

        for key in kwargs:
            self.root.set(key, kwargs[key])

    def setDescription(self, Description):
        assert type(Description) == str
        if self.Desc == None:
            self.Desc = etree.SubElement(self.root, 'Description')
            self.root.append(self.Desc)
        self.Desc.text = etree.CDATA(Description)

    def setParent(self, parent):
        pass

    def getLocalRoot(self):
        return self.root

    def __str__(self):
        return etree.tostring(self.root, pretty_print = True, xml_declaration = True, encoding = "UTF-8", standalone = "yes")

    def writeToFile(self, fileName = os.getcwd() + "/L5X_Printable.L5X"):
        tree = etree.ElementTree(self.root)
        tree.write(fileName, pretty_print = True, xml_declaration = True, encoding = "UTF-8", standalone = "yes")
