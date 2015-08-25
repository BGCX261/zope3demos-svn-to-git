from zope.interface import implements
from interfaces import IPerson, IPages, IArticle, INonsens
from zope.schema.fieldproperty import FieldProperty


class Person:
    """The Person object."""

    implements(IPerson)


class Pages:
    """The Pages object."""

    implements(IPages)


class Article:
    """The article object."""

    implements(IArticle)
    author = FieldProperty(IArticle['author'])
    title = FieldProperty(IArticle['title'])
    pages = FieldProperty(IArticle['pages'])

class Nonsens:
    """The nonsens object."""

    article = FieldProperty(INonsens['article'])

    implements(INonsens)