from zope.interface import Interface
from zope.schema import TextLine, Int, Object


class IPerson(Interface):

    lastname = TextLine(
        title=u"Lastname",
        description=u"Please give the lastname.",
        required=False)

    firstname = TextLine(
        title=u"Firstname",
        description=u"Please give the firstname.",
        required=False)


class IPages(Interface):

    start = Int(
        title=u"Start page",
        description=u"Please give the start page.",
        required=False)

    end = Int(
        title=u"End page",
        description=u"Please give the end page.",
        required=False)


class IArticle(Interface):

    author = Object(
        schema=IPerson,
        title=u"Author",
        description=u"The author of the article.",
        required=False)

    title = TextLine(
        title=u"Article title",
        description=u"Please give the title of the article.",
        required=False)

    pages = Object(
        schema=IPages,
        title=u"Pages",
        description=u"Start and end page of the article.",
        required=False)


class INonsens(Interface):

    article = Object(
        schema=IArticle,
        title=u"Article",
        description=u"A (nonsens) article",
        required=False)