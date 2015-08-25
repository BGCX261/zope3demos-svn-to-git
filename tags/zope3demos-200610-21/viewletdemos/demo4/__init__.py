from zope.app import pagetemplate
import zope.component
from zope.publisher.browser import BrowserView
import os

class MasterpageView(BrowserView):

    content = pagetemplate.ViewPageTemplateFile('page.pt')

    def __call__(self):
        view = zope.component.getMultiAdapter( (self.context, self.request), name='masterpage.html')
        view.content = self.content
        return view()

    sourcedir = os.path.dirname(__file__)
