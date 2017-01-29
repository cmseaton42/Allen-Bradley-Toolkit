try:
    import lxml
    from lxml import etree
except ImportError as e:
    print e.message

def setAsTarget(template):
    template.root.set("use", "Target")

def setAsContext(template):
    template.root.set("use", "Context")
