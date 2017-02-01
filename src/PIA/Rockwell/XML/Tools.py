try:
    import lxml
    from lxml import etree
except ImportError as e:
    print e.message

def setAsTarget(template):
    template.root.set("use", "Target")

def setAsContext(template):
    template.root.set("use", "Context")

def isValidTag(TagName):
    strCopy = TagName
    if "_" in strCopy: strCopy = strCopy.replace("_", "")
    if strCopy[0].isdigit(): return False
    return strCopy.isalnum()
