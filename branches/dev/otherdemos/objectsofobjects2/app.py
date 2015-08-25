from zope import interface, schema
from persistent import Persistent
from persistent.list import PersistentList

class IPerson(interface.Interface):
    first = schema.TextLine(title=u"firstname")
    last = schema.TextLine(title=u"lastname")

class Person(Persistent):
    interface.implements(IPerson)

class IAddressBook(interface.Interface):
    title = schema.TextLine(title=u'Title', required=False)

    persons = schema.List(title=u'Persons',
                          value_type=schema.Object(IPerson, title=u'person'),
                          required=False)

class AddressBook(Persistent):
    interface.implements(IAddressBook)

    def __init__(self):
        # create a default title
        self.title="My Address Book"

    title = ''
    # don't forget to make lists persistent
    persons = PersistentList()


