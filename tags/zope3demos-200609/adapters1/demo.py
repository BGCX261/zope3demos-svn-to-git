
import persistent
import zope.interface


class IMyAdaptableContent(zope.interface.Interface):
    """ Content Marker """
    title = zope.schema.TextLine(title=u'title')

class IDescription(zope.interface.Interface):
    """ description """
    description = zope.schema.Text(title=u'description')

class MyAdaptableContent(persistent.Persistent):
    """ MyContent object """
    zope.interface.implements(IMyAdaptableContent)
    title = "unknown"

class Description(object):
    zope.interface.implements(IDescription)
    #zope.component.adapts(MyAdaptableContent)

    def __init__(self, context):
        self.context = context
        self.context.__description = "%s description" % self.context.__name__
        # this overwrites on every restart
        # would need to update this via a form
        # to show it's persistency

    @property
    def description(self):
        return self.context.__description

class MyView(object):
    def __init__(self, context, request):
        self.context, self.request = context, request

    def __call__(self):
        return IDescription(self.context).description

class MyAdaptableContent2(persistent.Persistent):
    """ MyContent object """
    zope.interface.implements(IMyAdaptableContent)
    title = "unknown 2"