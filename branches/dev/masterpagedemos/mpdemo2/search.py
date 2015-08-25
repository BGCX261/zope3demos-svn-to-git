
from base import BaseView
from interfaces import ISearchView
from zope.interface import implements
from zope.viewlet.viewlet import ViewletBase
import zope.viewlet.interfaces
from zope.viewlet.manager import ViewletManagerBase

class SearchView(BaseView):
    implements(ISearchView)
    mastertemplate="masterb.pt"

class SearchViewManager(ViewletManagerBase):
    """ Viewlet manager """

class SearchViewlet(ViewletBase):
    """ SearchViewlet """

    viewletNamespace ="viewletNamespace result"

    def update(self):
        query = self.request.form.get('query')
        if query:
            self.results ="""you're query is "%s" """ % query
        else:
            self.results = "Type in a query"
