try:
    import lxml
    from lxml import etree
except ImportError as e:
    print e.message

ILLEGAL_CHARS['']

def setAsTarget(template):
    template.root.set("use", "Target")

def setAsContext(template):
    template.root.set("use", "Context")

def isValidTag(TagName):
