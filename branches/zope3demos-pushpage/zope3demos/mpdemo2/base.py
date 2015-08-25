# this is an implementation of masterpages based on the work of
# Juergen Kartnaller as reported by Stephan Richter
# http://www.nabble.com/Alternatives-to-macros-t2267984.html#a6303373

from interfaces import IMyProjectView
from zope.interface import implements
from zope.app.pagetemplate import ViewPageTemplateFile
import os

class BaseView(object):
    """ The base view for all views in my project. """
    implements(IMyProjectView)
    mastertemplate = "master.pt"

    def __call__(self, **args):
        return ViewPageTemplateFile(self.mastertemplate)(self,**args)

    sourcedir = os.path.dirname(__file__) # ignore: used to view source

class MainView(BaseView):
    """The main view used for the main index page."""

