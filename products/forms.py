from django import forms
from .widgets import CustomClearableFileInput
from .models import (Product, Category, Subcategory, Colour, 
                    Product_Subscription, Subscriptions, Subscription_Type, Sizes)


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('code', 'name', 'description',
                  'category', 'subcategory', 'subscription',
                  'has_sizes', 'colour',)

    image = forms.ImageField(label='Image',
                             required=False,
                             widget=CustomClearableFileInput)

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


class ProductSubsForm(forms.ModelForm):

    class Meta:
        model = Product_Subscription
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        subs_type = Subscription_Type.objects.all()
        subtype_friendly_names = [(st.id, st.get_name()) for st in subs_type]
        sizes = Sizes.objects.all()
        sizes_friendly_names = [(sz.id, sz.get_name()) for sz in sizes]

        self.fields['subscription_type'].choices = subtype_friendly_names
        self.fields['size'].choices = sizes_friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = ('rounded-2')


class SubscriptionsForm(forms.ModelForm):

    class Meta:
        model = Subscriptions
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        product = Product.objects.all()
        product_friendly_names = [(p.id, p.name) for p in product]
        prod_sub = Product_Subscription.objects.all()
        prod_sub_friendly_names = [(ps.id, ps.get_name()) for ps in prod_sub]

        self.fields['product'].choices = product_friendly_names
        self.fields['product_sub'].choices = prod_sub_friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = ('rounded-2')