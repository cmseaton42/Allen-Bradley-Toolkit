try:
    import lxml
    from lxml import etree
except ImportError as e:
    print e.message

from PIA.Rockwell.XML.Tools import *
from Base_Template import Base_Template

class Project(Base_Template):
    '''
    Project Template:
    See L5X Manual for Details,
    These members are to be used when defining a project.
    ----------------------------------------------------------
    This class should always serve as the base class.
    ----------------------------------------------------------
    For Information on this see the provided L5X Manual from Rockwell
    '''
    def __init__(self, SchemaRevision = "1.0", SoftwareRevision = "30.00"):
            #Initialize Member Attributes
            self.root = etree.Element("RSLogix5000Content")
            self.root.set("SchemaRevision", SchemaRevision)
            self.root.set("SoftwareRevision", SoftwareRevision)

    def getControllerRoot(self):
        return self.Controller

    def setController(self, Controller):
        assert etree.iselement(Controller.getLocalRoot()) and Controller.getLocalRoot().tag == "Controller"
        self.root.append(Controller.getLocalRoot())

    def setAttribute(self, kwargs):
        for key in kwargs:
            self.root.set(key, kwargs[key])
