
import pushpage.browser
from pushpage.browser import PushPageFactory
import os, sys

# utility
def openTemplate(template):
    """ utility """
    if type(template)==type(str()):
        if template.endswith('.pt'):
            f = open( "%s/%s" % (os.path.dirname(__file__), template))
            template = f.read()
            f.close()
        return template
    else:
        return template()

# decorator
class push:
    """ Pushpage decorator """
    __namespace__ = {}

    def __init__(self, template):
        self.template = openTemplate(template)

    def update(self):
        self.__namespace__ = self.data
        self.__namespace__['context'] = self.context
        self.__namespace__['request'] = self.request

    def basenamespace(self, context, request):
        return self.__namespace__

    def render(self):
        factory = PushPageFactory(self.template, self.basenamespace)
        return factory(self.context, self.request)()

    def __call__(self, f):
        def fname(*args, **kw ):
            # my favorite hack
            locals = sys._getframe(1).f_locals
            self.context = locals.get('context')
            self.request = locals.get('request')
            self.data = { 'contents' : f(*args) }
            self.update() #viewlet compliance
            return self.render()
        return fname

class PushPageView(object):
    def __init__(self, context, request):
        self.context, self.request = context, request

    def __call__(self):
        return self.render(self.context, self.request)

# mapping
def templateData(context, request):
    """ Used for pushpage1.html """
    data = {'context': context,
            'request': request}
    results = []
    for name, item in context.items():
        results.append(name)
    data.update({'folder': '\n*'.join(results)})
    return data


class pushPage2(object):

    def left_slot(self):
        return self.__namespace__.update( {'left_slot': [self.context.__name__]} )

    def __init__(self, context, request):
        self.context, self.request = context, request
        self.__namespace__ = {}

    def namespace(self, context, request):
        return self.__namespace__

    def update(self):
        self.left_slot()

    @property
    def template(self):
        return """<div tal:replace="left_slot" />"""

    def render(self):
        factory = PushPageFactory(self.template, self.namespace)
        return factory(self.context, self.request)()

    def __call__(self):
        self.update()
        return self.render()


class namespace:
    """ return namespace as a class """
    def __init__(self, name):
        self.name = name

    def __call__(self, f):
        def fname(*args):
            data = { self.name: f(*args) }
            data['context'] = args[0]
            data['request'] = args[1]
            return data
        return fname

@namespace('contents')
def list_contents(context, request):
    contents = [item for name, item in context.items()]
    return contents

list_contents_tmpl ="""
[[[[<li tal:repeat="content contents" tal:content="structure content/__name__" />]]]]
"""


list_contents_tmpl2 ="""
<h2> list_contents_tmpl2 </h2>
<li tal:repeat="content contents" tal:content="structure content/__name__" />
"""

show_contents = """
<p tal:replace="structure contents" />

"""

apage ="""
<html><body>
          <li tal:repeat="rs contents/right_slot" tal:content="structure rs" />
          <span tal:replace="structure contents/middle_slot" />
</body></html>"""

@push('page2.pt')
def list_contents2(context, request):
    contents = [item for name, item in context.items()]
    return contents


class PushPage4(object):
    """ A PushPage view that uses the @push decorator

    1. can this now also be a registered viewlet as well?

    """

    def __init__(self, context, request):
        self.context, self.request = context, request

    @push(apage)
    def render(self, context, request):
        data = {}
        data['right_slot']= [list_contents2(context, request), list_contents2(context, request)]
        data['middle_slot']= list_contents2(context, request)
        return data

    def __call__(self):
        return self.render(self.context, self.request)



class PushPage5(object):
    """ A PushPage view that uses the @push decorator

    1. can this now also be a registered viewlet as well?

    """

    def __init__(self, context, request):
        self.context, self.request = context, request

    def page1(self):
        return "page1"

    @push(show_contents)
    def page2(self):

        @push(show_contents)
        def p1():
            return "<li>this is p1</li>"

        @push(show_contents)
        def p2():
            return "<li>this is p2</li>"

        results = p1() + p2()
        return results

    @push(apage)
    def render(self, context, request):
        data = {}
        data['right_slot']= [list_contents2(context, request), list_contents2(context, request)]
        data['middle_slot']= list_contents2(context, request)
        return data

    def __call__(self):
        return self.render(self.context, self.request)



class MasterPage1(object):
    """ Attempt at hooking in a masterpage

    """

    def __init__(self, context, request):
        self.context, self.request = context, request

    def page1(self):
        return "page1"

    @push(show_contents)
    def page2(self):
        return """ success from masterpage1 page2
       """

        results = p1() + p2()
        return results

    @push(apage)
    def render(self, context, request):
        data = {}
        data['right_slot']= [list_contents2(context, request), list_contents2(context, request)]
        data['middle_slot']= list_contents2(context, request)
        return data

    def __call__(self):
        return self.render(self.context, self.request)