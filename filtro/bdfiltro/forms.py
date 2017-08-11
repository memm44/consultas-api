from django import forms


class Form_opcion(forms.Form):
    opcion = forms.CharField(max_length=2)
