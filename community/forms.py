from django import forms
from .models import Discussions, Discussion_Comments
from products.models import Product


class DiscussionsForm(forms.ModelForm):

    class Meta:
        model = Discussions
        fields = ('product', 'topic', 'disc_topic_text',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'product': 'Product',
            'topic': 'Topic Title',
            'disc_topic_text': 'Disucussion Details',
        }
        product = Product.objects.all()
        product_friendly_names = [(p.id, p.get_name()) for p in product]

        self.fields['product'].choices = product_friendly_names
        self.fields['topic'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = ('rounded-2'
                                                        'stripe-style-input')
            self.fields[field].label = False


class Discussions_CommentsForm(forms.ModelForm):

    class Meta:
        model = Discussion_Comments
        fields = ('comment',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'comment': 'Comments',
        }
        
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = ('rounded-2'
                                                        'stripe-style-input')
            self.fields[field].label = False
