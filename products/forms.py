from django import forms
from .models import Product, Category, Subcategory, Colour


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('code', 'name', 'description',
                  'category', 'subcategory', 'subscription',
                  'has_sizes', 'colour',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        cat_friendly_names = [(c.id, c.get_name()) for c in categories]
        subcategories = Subcategory.objects.all()
        subcat_friendly_names = [(s.id, s.get_name()) for s in subcategories]
        colours = Colour.objects.all()
        colour_friendly_names = [(cl.id, cl.get_name()) for cl in colours]

        self.fields['category'].choices = cat_friendly_names
        self.fields['subcategory'].choices = subcat_friendly_names
        self.fields['colour'].choices = colour_friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = ('rounded-2')
