import zope.viewlet.interfaces
import zope.interface
from zope.viewlet.manager import ViewletManagerBase
import zope.contentprovider.interfaces
from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from zope.publisher.browser import BrowserView
import os
from zope.app import pagetemplate
import zope.component

def htmlquote(source):
    source = source.replace('>', '&gt;')
    source = source.replace('<', '&lt;')
    source = source.replace('--&gt;', '-->')
    source = source.replace('&lt;!--', '<!--')
    return source

class MasterpageView(BrowserView):

    def __call__(self):
        view = zope.component.getMultiAdapter( (self.context, self.request), name='masterpage.html')
        view.content = self.content
        return view()

    sourcedir = os.path.dirname(__file__)

class RedirectView(object):

    def __init__(self, context, request):
        self.context, self.request = context, request

    def __call__(self):
        self.request.redirect('/@@z3d.index.html')


class SourceScriptContentProvider:
    zope.interface.implements(zope.contentprovider.interfaces.IContentProvider)
    zope.component.adapts(zope.interface.Interface,
                          IDefaultBrowserLayer,
                          zope.interface.Interface)
    def __init__(self, context, request, view):
        self.__parent__, self.context, self.request = view, context, request

    def update(self):
        pass

    def render(self):
        return """
     <script language="javascript" src="/@@/zdjs/shCore.js"></script>
     <script language="javascript" src="/@@/zdjs/shBrushPython.js"></script>
     <script language="javascript" src="/@@/zdjs/shBrushXml.js"></script>

     <script language="javascript">
         dp.SyntaxHighlighter.HighlightAll('code');
     </script>
   """

class ISources(zope.interface.Interface):
    relativePath = zope.schema.TextLine(title=u'Relative path')
    sources = zope.schema.TextLine(title=u'Sources')

class ViewSourceContentProvider:
    zope.interface.implements(ISources)
    zope.component.adapts(zope.interface.Interface,
                          IDefaultBrowserLayer,
                          zope.interface.Interface)
    relativePath=''
    sources=''

    def __init__(self, context, request, view):
        self.__parent__, self.context, self.request = view, context, request

    def update(self):
        sources= []
        # this is a bit of magic to get the directory
        # of the PageView class, for an example
        # see mpdemo1.demo.PageView.sourcedir

        sourcedirname = self.__parent__.sourcedir
        for sourcename in self.sources.split():
            ext = os.path.splitext(sourcename)[-1]
            sourcetype=None
            if ext in ['.zcml']:
                sourcetype = 'xml'
            if ext in ['.pt']:
                sourcetype = 'html'
            if ext in ['.py']:
                sourcetype = 'py'
            sourcefile = open(sourcedirname + '/'  + sourcename )
            source = [line.rstrip() for line in sourcefile.readlines()]
            source = '\n'.join(source)
            sourcefile.close()
            sources.append('<h4>%s</h4><form><textarea name="code" class="%s" cols="60" rows="10">%s</textarea></form>' % (sourcename, sourcetype, htmlquote(source)))
        self.results = "\n".join(sources)

    def render(self):
        return self.results

