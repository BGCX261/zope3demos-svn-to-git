# for convenince sake we put all of the
# interfaces, components and views in the
# same module

import zope.viewlet.interfaces
from zope.viewlet.manager import ViewletManagerBase
import zope.viewlet.viewlet

class IDemoViewletManager(zope.viewlet.interfaces.IViewletManager):
    """ Marker """

class DemoViewletManager(ViewletManagerBase):
    """ IDemoViewletManager marker interface """
    zope.interface.implements(IDemoViewletManager)



    def update(self):
        shownColumns=['name4', 'size4']
        rows = []
        for name, value in self.context.items():
            rows.append(
                [zope.component.getMultiAdapter(
                     (value, self.request, self.__parent__, self),
                    zope.viewlet.interfaces.IViewlet, name=colname)
                 for colname in shownColumns])
            [entry.update() for entry in rows[-1]]
        self.viewlets = rows

class NameViewlet(zope.viewlet.viewlet.ViewletBase):

    def render(self):
        return "<b>%s</b>" % self.context.__name__

class SizeViewlet(zope.viewlet.viewlet.ViewletBase):

    def render(self):
        return zope.size.interfaces.ISized(self.context).sizeForDisplay()


