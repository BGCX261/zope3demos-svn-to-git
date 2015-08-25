from zope.app.form import CustomWidgetFactory
from zope.app.form.browser import ObjectWidget
from zope.app.form.browser import ListSequenceWidget,SequenceWidget
from zope.formlib import form
from app import Person, IAddressBook, AddressBook


person_widget = CustomWidgetFactory(ObjectWidget, Person)
persons_widget = CustomWidgetFactory(ListSequenceWidget, subwidget=person_widget)

class EditFormView(form.EditForm):
    form_fields = form.Fields(IAddressBook, render_context=True)
    form_fields['persons'].custom_widget = persons_widget