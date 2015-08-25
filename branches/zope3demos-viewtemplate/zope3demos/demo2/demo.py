
import zope.viewlet.interfaces



class IDemoViewletManager(zope.viewlet.interfaces.IViewletManager):
    """ IViewletManager marker interface """

class Viewlet(object):
    """ Demo2 viewlet 1"""

    def __init__(self, context, request, view, manager):
        self.__parent__ = view

    def update(self):
        pass

    def render(self):
        return u'<b>Viewlet1 in class</b>'

# note: viewlet2 is a ZPT template without a viewlet class

class Viewlet3(object):
    """ Demo3 viewlet 3 """

    classnamespacetest = "class namespace test success!"

    def update(self):
        pass

    def __init__(self, context, request, view, manager):
        self.__parent__ = view
        self.context, self.request = context, request





