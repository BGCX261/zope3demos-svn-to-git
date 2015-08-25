
from zope.viewlet import interfaces
import zope.viewlet.interfaces
from zope.app.pagetemplate import ViewPageTemplateFile
from zope.interface import implements, Interface
from zope.viewlet.manager import ViewletManagerBase
import os

class IBaseViewletManager(zope.viewlet.interfaces.IViewletManager):
    """IViewletManager"""

class BaseViewletManager(ViewletManagerBase):
    """ base view """


class BasePage(object):
    """ The base view for all views in my project. """
    mastertemplate = "master.pt"

    __call__ = ViewPageTemplateFile(mastertemplate)

    sourcedir = os.path.dirname(__file__) # ignore: used to view source

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


def MyMapping(context, request):
    return {'context': context, 'request': request}