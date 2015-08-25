import zope.viewlet.interfaces
import zope.schema
import zope.interface



class IContentManager(zope.viewlet.interfaces.IViewletManager):
    """ Viewlet manager """


# currently these are basically all marker interfaces

class IMyProjectView(zope.interface.Interface):
    """ Currently a marker interface """

class IMyProjectMain(zope.interface.Interface):
    """ Currently a marker interface """

class ISearchView(zope.interface.Interface):
    """ Search view interfaces """

