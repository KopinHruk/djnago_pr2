from django import forms
from .models import Item, Row
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Div, HTML
from django.forms import inlineformset_factory


class ExampleFormSetHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(ExampleFormSetHelper, self).__init__(*args, **kwargs)
        self.form_method = 'post'
        self.layout = Layout(
            Div(Field('row_name', required=True),
                Field('deadline', required=True),
                Field('is_completed'),
                css_class='form_row')
        )
        #self.render_required_fields = True
        self.form_tag = False


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        #self.helper.render_required_fields = True
        self.helper.form_tag = False


CreateRowFormSet = inlineformset_factory(Item, Row, fields='__all__', extra=4)
UpdateRowFormSet = inlineformset_factory(Item, Row, fields='__all__', extra=0)
