from zope.app.catalog.interfaces import ICatalog
from zope.app import zapi

from hurry.query.query import Query, Text
from hurry.query.interfaces import IQuery
from hurry.query import set as setquery
from hurry.query import query

class CatView(object):

    def __init__(self, context, request):
        self.context, self.request = context, request

    def __call__(self):

        q = zapi.getUtility(IQuery)

        # you'll need to setup an initd utility
        # and a catalog registered as 'cat1'
        s = query.Text(('cat1','zpts'), 'test')
        r = q.searchResults(s)
        results = []

        return "test %s " % str([e.__name__ for e in list(r)])

class CatView2(object):
    """ """

    def __init__(self, context, request):
        self.context, self.request = context, request

    def __call__(self):
        return ""
