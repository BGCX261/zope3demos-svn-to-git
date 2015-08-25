from zope.interface import implements, Interface
from zope.component import adapts, provideAdapter
from persistent import Persistent
from zope.contentprovider.interfaces import IContentProvider
from zope.publisher.interfaces.browser import IDefaultBrowserLayer

class MyContentProvider:
    implements(IContentProvider)
    adapts(Interface, IDefaultBrowserLayer, Interface)

    def __init__(self, context, request, view):
        self.context = context
        self.request = request
        self.__parent__ = view

    def update(self):
        pass

    def render(self):
        return u'MyContentProvider success from cpdemo1'






