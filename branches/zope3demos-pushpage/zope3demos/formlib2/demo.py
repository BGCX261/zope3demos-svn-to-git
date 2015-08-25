# formlib demos


from zope import interface, schema
from zope.formlib import form
import datetime
import persistent


class IOrder(interface.Interface):
    identifier = schema.Int(title=u"Identifier", readonly=True)
    name = schema.TextLine(title=u"name")
    min_size = schema.Float(title=u"Minimum size")
    max_size = schema.Float(title=u"Maximum size")
    now = schema.Datetime(title=u'Now', readonly=True)

    @interface.invariant
    def maxGreaterThanMin(order):
        if order.max_size < order.min_size:
            raise interface.Invalid("Maximum is less than minimum")

class OrderView(object):
    """ holder """



class Order(persistent.Persistent):
    interface.implements(IOrder)

    identifier ="unknown"
    name = "unknown"
    min_size =0.0
    max_size = 0.0
    now = property(lambda self: datetime.datetime.now())

class Formlib(form.EditForm):
    form_fields = form.Fields(IOrder, omit_readonly=True, render_context=True)



