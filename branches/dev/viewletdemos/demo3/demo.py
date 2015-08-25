# for convenience sake we put all of the
# interfaces, components and views in the
# same module

import zope.viewlet.interfaces
from zope.viewlet.manager import ViewletManagerBase
from zope.app import zapi
from zope.app.traversing.browser.interfaces import IAbsoluteURL

class IDemoViewletManager(zope.viewlet.interfaces.IViewletManager):
    """ Marker """

class DemoViewletManager(ViewletManagerBase):
    """ IDemoViewletManager marker interface """
    zope.interface.implements(IDemoViewletManager)

    def update(self):
        rows=[]

        # list all in this directory
        for name, object in self.context.items():

            # adapt each folder item to IViewlet
            rows.append(
               zope.component.getMultiAdapter(
                      (object, self.request, self.__parent__, self),
                      zope.viewlet.interfaces.IViewlet, name='z3d.demo3.viewlet')
                   )
        [entry.update() for entry in rows]
        self.viewlets = rows

class NameViewlet(object):
    """ Demo3 viewlet """

    def __init__(self, context, request, view, manager):
        self.__parent__ = view
        self.context = context
        self.request= request
    def update(self):
        pass
    def render(self):
        url = zapi.getMultiAdapter( (self.context, self.request), IAbsoluteURL)
        return "<li>IAbsoluteUrl == %s</li>" % url

class IDemo3SourceViewletManager(zope.viewlet.interfaces.IViewletManager):
    """ FIXME: A hack to make source view work """





