from zope.app import pagetemplate
import zope.component
from zope.publisher.browser import BrowserView
import os

class PageView(BrowserView):

    content = pagetemplate.ViewPageTemplateFile('page.pt')

    testMessage = "a test message from PageView class"

    def ls(self):
        """  list all items in the folder """
        return [name for name, object in self.context.items()]

    def __call__(self):
        view = zope.component.getMultiAdapter( (self.context, self.request), name='masterpage1.html')
        view.content = self.content
        view.sourcedir = __file__
        return view()

    sourcedir = os.path.dirname(__file__) # ignore: used to view source

