from zope.app.form.browser.editview import EditView
from zope.app.form import CustomWidgetFactory
from zope.app.form.browser import ObjectWidget, TextWidget
from zope.schema import TextLine

from interfaces import INonsens,IArticle
from article import Person, Pages, Article


class Article_w(ObjectWidget):
    """This is the 'medium' class which inherits ObjectWidget
    and in which ObjectWidgets are defined."""

    __used_for__ = IArticle

    author_widget = CustomWidgetFactory(ObjectWidget, Person)
    # (Note that you don't have do define a custom widget for the simple TextLine 'title'!)
    pages_widget = CustomWidgetFactory(ObjectWidget, Pages)


class NonsensEditView(EditView):
    """This is the customized EditView class."""

    __used_for__ = INonsens

    #Give the 'medium' class Article_w as an argument to the contructor of CustomWidgetFactory.
    article_widget = CustomWidgetFactory(Article_w, Article)