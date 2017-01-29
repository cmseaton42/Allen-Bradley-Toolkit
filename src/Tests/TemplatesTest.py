import sys
import os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from lib.PIA.Rockwell.Types import CommonType
from lib.PIA.Rockwell.XML.Templates import *

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

if __name__ == '__main__':
    MemberTest()
