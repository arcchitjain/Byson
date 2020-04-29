from django.forms import forms, CharField, ImageField


class NameForm(forms.Form):
    shop_name = CharField(label='Shop name', max_length=100)


class ImageForm(forms.Form):
    image = ImageField(label='Image', required=False)
