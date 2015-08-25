from zope.interface import Interface, implements
from zope import viewlet
from z3c.viewtemplate.baseview import BaseView


class IDemoPage(Interface):
    """ A view marker """

class DemoPage(BaseView):
    """And example of a page. You really only need the class to have a
       registration point.

    The view the content provider is registered for.
    The view can either be an interface or a class. By default the provider
    is registered for all views, the most common case.
    """
    # IDemoPage is a convenient way to mark pages that get rendered
    # by the masterpage
    implements(IDemoPage)

class IContentViewletManager(viewlet.interfaces.IViewletManager):
    """ The interface of the view this viewlet is for. (default IBrowserView) """


class DemoViewlet(BaseView):
    """ A class that provides attributes used by the viewlet.

    In this case, we're providing a content function"""

    def content(self):
        return """ this is DemoViewlet.content() %s """ % self.context.__name__
    
class DemoViewlet2(BaseView):
    """ A class that provides attributes used by the viewlet.

    In this case, we're providing a content function"""

    def content(self):
        return """ this is DemoViewlet2.content() %s """ % self.context.__name__