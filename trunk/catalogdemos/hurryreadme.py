from datetime import datetime
from zope.interface import Interface, Attribute, implements
class IContent(Interface):
    f1 = Attribute('f1')
    f2 = Attribute('f2')
    f3 = Attribute('f3')
    f4 = Attribute('f4')
    t1 = Attribute('t1')
    t2 = Attribute('t2')
  
from zope.app.container.contained import Contained

class Content(Contained):
    implements(IContent)
    def __init__(self, id, f1='', f2='', f3='', f4='', t1='', t2=''):
        self.id = id
        self.f1 = f1
        self.f2 = f2
        self.f3 = f3
        self.f4 = f4
        self.t1 = t1
        self.t2 = t2
    def __cmp__(self, other):
        return cmp(self.id, other.id)
    
from zope import interface
import zope.app.intid.interfaces
from zope.app.testing import ztapi
from zope.app.catalog.interfaces import ICatalog
from zope.app.catalog.catalog import Catalog
catalog = Catalog()
ztapi.provideUtility(ICatalog, catalog, 'catalog1')

from zope import interface
import zope.app.intid.interfaces
from zope.app.testing import ztapi
class DummyIntId(object):
    interface.implements(zope.app.intid.interfaces.IIntIds)
    MARKER = '__dummy_int_id__'
    def __init__(self):
        self.counter = 0
        self.data = {}
    def register(self, obj):
        intid = getattr(obj, self.MARKER, None)
        if intid is None:
            setattr(obj, self.MARKER, self.counter)
            self.data[self.counter] = obj
            intid = self.counter
            self.counter += 1
        return intid
    def getObject(self, intid):
        return self.data[intid]
    def __iter__(self):
        return iter(self.data)
intid = DummyIntId()
ztapi.provideUtility(
    zope.app.intid.interfaces.IIntIds, intid)

from zope.app.catalog.field import FieldIndex
from zope.app.catalog.text import TextIndex
catalog['f1'] = FieldIndex('f1', IContent)
catalog['f2'] = FieldIndex('f2', IContent)
catalog['f3'] = FieldIndex('f3', IContent)
catalog['f4'] = FieldIndex('f4', IContent)
catalog['t1'] = TextIndex('t1', IContent)
catalog['t2'] = TextIndex('t2', IContent)

content = [
Content(1, 'a', 'b', 'd'),
Content(2, 'a', 'c'),
Content(3, 'X', 'c'),
Content(4, 'a', 'b', 'e'),
Content(5, 'X', 'b', 'e'),
Content(6, 'Y', 'Z')]

print content

from hurry.query.query import Query
from hurry.query.interfaces import IQuery
ztapi.provideUtility(IQuery, Query())
  
from zope.app import zapi
from hurry.query.interfaces import IQuery
def displayQuery(q):
    query = zapi.getUtility(IQuery)
    r = query.searchResults(q)
    return [e.id for e in sorted(list(r))]

d1 = datetime.now()
initd = DummyIntId()
ztapi.provideUtility( zope.app.intid.interfaces.IIntIds, intid)
from zope.app.catalog.interfaces import ICatalog
from zope.app.catalog.catalog import Catalog
catalog = Catalog()
ztapi.provideUtility(ICatalog, catalog, 'catalog1')
from zc.catalog.catalogindex import SetIndex
catalog['f1'] = SetIndex('f1', IContent)
catalog['f2'] = FieldIndex('f2', IContent)
print catalog



d2 = datetime.now()
print d1, d2
content = [
Content(1, ['a', 'b', 'c'], 1),
Content(2, ['a'], 1),
Content(3, ['b'], 1),
Content(4, ['c', 'd'], 2),
Content(5, ['b', 'c'], 2),
Content(6, ['a', 'c'], 2),
Content(7, [d1.strftime('%m-%b-%d'), d2.strftime('%m-%b-%d'), 'a'], 2)
]

print content

for entry in content:
    catalog.index_doc(intid.register(entry), entry)
f1 = ('catalog1', 'f1')
from hurry.query.set import AnyOf
print displayQuery(AnyOf(f1, ['a','c']))
print "*"*8
print displayQuery(AnyOf(f1, [d1.strftime('%m-%b-%d')]))
