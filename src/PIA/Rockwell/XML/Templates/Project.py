try:
    import lxml
    from lxml import etree
except ImportError as e:
    print e.message

from PIA.Rockwell.XML.Tools import *

class Project():
    '''
    Project Template:
    See L5X Manual for Details,
    These members are to be used when defining a datatype.
    ----------------------------------------------------------
    For Information on this see the provided L5X Manual from Rockwell
    '''
    def __init__(self, SchemaRevision = "1.0", SoftwareRevision = "30.00"):
            #Initialize Member Attributes
            self.root = etree.Element("RSLogix5000Content")

    def getControllerRoot(self):
        return self.Controller

    def checkIfChild(self, nodeTag):
        assert type(nodeTag) == str
        for node in self.root:
            if node.tag == NodeTag: return False
        return True

    def addController(self, Controller):
        assert etree.iselement(Controller.getLocalRoot()) and Controller.getLocalRoot().tag == "Controller"
        if not self.checkIfChild("Controller"):
            self.Controller = etree.SubElement(self.root, "Controller")
        self.Controller.append(Datatype)

    def setAttribute(self, **kwargs):
        for key in kwargs:
            self.root.set(key, kwargs[key])

    def getLocalRoot(self):
        return self.root

    def __str__(self):
        return etree.tostring(self.root, pretty_print = True)
