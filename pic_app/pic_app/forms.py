from django import forms

from pic_app.models import Picture_colour


class Picture_colourForm(forms.ModelForm):
    class Meta:
        model = Picture_colour
        fields = ('image', 'colour_hex', )
