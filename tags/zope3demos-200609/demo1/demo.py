import zope.viewlet.interfaces

class IViewletManager(zope.viewlet.interfaces.IViewletManager):
    """IViewletManager"""

class Viewlet(object):

    def __init__(self, context, request, view, manager):
        self.__parent__ = view

    def render(self):
        return u'Demo1Viewlet success!'



