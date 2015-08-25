# formlib demos


from zope import interface, schema
from zope.formlib import form


class IOrder(interface.Interface):
    identifier = schema.Int(title=u"Identifier", readonly=True)
    name = schema.TextLine(title=u"name")
    min_size = schema.Float(title=u"Minimum size")
    max_size = schema.Float(title=u"Maximum size")
    now = schema.Datetime(title=u'Now', readonly=True)


class Formlib1:
    form_fields = form.Fields(IOrder, omit_readonly=True)

    def __init__(self, context, request):
        self.context, self.request = context, request

    def __call__(self, ignore_request=False):
        # this sets up default widgets
        widgets = form.setUpWidgets(
            self.form_fields, 'form', self.context, self.request, ignore_request=ignore_request)
        return '\n'.join([w() for w in widgets])

    def length(self):
        return str( len(self.form_fields) )

    def name(self):
        result = ''
        query = self.request.get('query','')
        if query:
            try:
                result = self.form_fields[query].__name__
            except:
                names = [w.__name__ for w in self.form_fields]
                result = "INVALID QUERY: use one of %s" % names
        return """
    <html><body>
    <form>
    <input name="query" value=""><input type=submit value=submit>
    </form>
    %s
    </body></html>
    """ % result


class Formlib2:
    """
    Reading Data
    ============
    Of course, we don't just want to display inputs.  We want to
    get the input data.  We can use getWidgetsData for that:
    """

    form_fields =form.Fields(IOrder, omit_readonly=True)

    def __init__(self, context, request):
        self.context, self.request = context, request

    def __call__(self):
        widgets = form.setUpWidgets(
                self.form_fields, 'form', self.context, self.request)
        results = []
        data ={}
        if 'submit' in self.request:
            # get input data
            errors = form.getWidgetsData(widgets, 'form', data)
            if errors:
                results.append('<h4>there were errors</h4>')

        for w in widgets:
            results.append("<p>%s</p>" % w())
            error = w.error()
            if error:
                results.append("<p style='color:red'>%s</p>" % error)

        results = '\n'.join(results)
        return """<html><body>
        <form>%s <input type="submit" name="submit" value="submit"></form>
        <p>updated: %s</p>
        </body></html>
        """ % (results, str(data))


class IOrder3(interface.Interface):
    identifier = schema.Int(title=u"Identifier", readonly=True)
    name = schema.TextLine(title=u"name")
    min_size = schema.Float(title=u"Minimum size")
    max_size = schema.Float(title=u"Maximum size")
    now = schema.Datetime(title=u'Now', readonly=True)

    @interface.invariant
    def maxGreaterThanMin(order):
        if order.max_size < order.min_size:
            raise interface.Invalid("Maximum is less than minimum")

class Formlib3:
    """
    Invariants
    ==========

    The `getWidgetsData` function checks individual field constraints.
    Interfaces can also provide invariants that we may also want to check.
    The `checkInvariants` function can be used to do that.

    In our order example, it makes sense to require that the maximum is
    greater than or equal to the minimum:
    """

    form_fields =form.Fields(IOrder3, omit_readonly=True)

    def __init__(self, context, request):
        self.context, self.request = context, request

    def __call__(self):
        widgets = form.setUpWidgets(
                self.form_fields, 'form', self.context, self.request)
        results = []
        data ={}
        if 'submit' in self.request:
            # get input data
            errors = form.getWidgetsData(widgets, 'form', data)
            invariant_errors = form.checkInvariants(self.form_fields, data)
            if errors:
                results.append('<h4>there were errors</h4>')

            if invariant_errors:
                results.append('<h4>there were invariant errors</h4>')
                for error in invariant_errors:
                    results.append( "<p style='color:red'>%s</p>" % error )

        for w in widgets:
            results.append("<p>%s</p>" % w())
            error = w.error()
            if error:
                results.append("<p style='color:red'>%s</p>" % error)

        results = '\n'.join(results)
        return """<html><body>
        <form>%s <input type="submit" name="submit" value="submit"></form>
        <p>updated: %s</p>
        </body></html>
        """ % (results, str(data))




