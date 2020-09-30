from django import forms
from .models import Discussions, Discussion_Comments
from products.models import Product


class DiscussionsForm(forms.ModelForm):

    class Meta:
        model = Discussions
        fields = ['topic', 'disc_topic_text']
        exclude = ('product', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'topic': 'Topic Title',
            'disc_topic_text': 'Discussion Details',
        }

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
        fields = ['comment']

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
