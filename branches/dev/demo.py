from zope import interface
from z3c.viewtemplate.baseview import BaseView

class IMyView(interface.Interface):
    """ My view """
    pass

class MyView(BaseView):
    """ Actual view class"""
    interface.implements(IMyView)

    def test(self):
        return "test xyz"

    def __init__(self,context, request):
        self.context, self.request = context, request