
from zope.viewlet import interfaces
import zope.viewlet.interfaces
from zope.app.pagetemplate import ViewPageTemplateFile
from zope.interface import implements, Interface
from zope.viewlet.manager import ViewletManagerBase
import os
from pushpage.browser import PushPageFactory
import zope.component

class IBaseViewletManager(zope.viewlet.interfaces.IViewletManager):
    """IViewletManager"""

class BaseViewletManager(ViewletManagerBase):
    """ base view """


class BasePage(object):
    """ The base view for all views in my project. """
    mastertemplate = "master.pt"

    __call__ = ViewPageTemplateFile(mastertemplate)

    sourcedir = os.path.dirname(__file__) # ignore: used to view source


class Page3(object):

    def getTest(self, context, request):
        return {'test': [self.context.__name__]}

    def __init__(self, context, request):
        self.context, self.request = context, request

    def __call__(self):
        TEMPLATE ="""<div tal:replace="test" />"""
        factory = PushPageFactory(TEMPLATE, self.getTest)
        page = factory(self.context, self.request)
        return page()

class IPage1(Interface):
    """ marker """

class Page1(BasePage):
    """ basic page """
    # must implement some interface
    # to be picked up by the viewlet manager
    implements(IPage1)


class IPage2(Interface):
    """ basic page """

class Page2(BasePage):
    """ basic page """
    implements(IPage2)

def xmapContentProviders(context, request, view, providers):
    data = {}
    for name in providers:
        provider = zope.component.getMultiAdapter((context, request, view),
                                             interfaces.IViewletManager, name=name)
        # Provide a useful error message, if the provider was not found.
        if provider is None:
            raise interfaces.ContentProviderLookupError(name)
        provider.update()
        data['%s' % name] = provider.render()
    return {'provider': data}

def AMapping(context, request, view):
    data = {'context': context,
            'request': request}
    data.update( pushpage.browser.mapContentProviders(context, request, view, ['dvm4'] ) )
    #provider = zope.component.getMultiAdapter((context, request, view),
    #                                         interfaces.IViewletManager, name='dvm4')
    #provider.update()
    #data = mapContentProviders(context, request, view, ['dvm4'] )
    return data

class MyMapping(object):

    def __init__(self,context, request):
        self.context, self.request = context, request
        self.__parent__ = self.context.__parent__
        self.__name__ = context.__name__
    def __call__(self):
        return {'context': self.context, 'request': self.request}