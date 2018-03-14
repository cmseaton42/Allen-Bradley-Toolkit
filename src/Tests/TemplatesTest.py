import sys
import os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from AB.Rockwell.Types import CommonType
from AB.Rockwell.XML.Templates import *

import lxml
from lxml import etree

def MemberTest():
    root = etree.Element('Members')

    desc = "Just a Test Tag"
    testMember1 = Member('someTag1', CommonType.INT, Description = desc)
    testMember2 = Member('someTag2', CommonType.STRING)

    testMember1.setParent(root)
    testMember2.setParent(root)

    print etree.tostring(root, pretty_print = True)

def DatatypeTest():
    root = etree.Element('Datatypes')

    dt = Datatype('Sample', Description = 'just for fun')

    memList = []

    memList.append(Member('sint0', CommonType.SINT, Description = 'some random sint'))
    memList.append(Member('sint1', CommonType.SINT, Description = 'blah'))

    for mem in memList:
        dt.addMember(mem)

    root.append(dt.getLocalRoot())

    print etree.tostring(root, pretty_print = True)

def TagTest():
    root = etree.Element('Tags')

    Tag1 = Tag('Hello_World', CommonType.BOOL)
    Tag2 = Tag('SomeOtherTag', CommonType.SINT)

    Tag1.setParent(root)
    Tag2.setParent(root)

    print etree.tostring(root, pretty_print = True)

if __name__ == '__main__':
    MemberTest()
    DatatypeTest()
    TagTest()
