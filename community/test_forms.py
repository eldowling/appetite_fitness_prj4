from django.test import TestCase
from community.forms import DiscussionsForm, Discussions_CommentsForm


class TestDiscussionsForm(TestCase):

    def test_item_topic_is_required(self):
        form = DiscussionsForm({'topic': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('topic', form.errors.keys())
        self.assertEqual(form.errors['topic'][0], 'This field is required.')

    def test_item_disc_topic_text_is_required(self):
        form = DiscussionsForm({'disc_topic_text': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('disc_topic_text', form.errors.keys())
        self.assertEqual(form.errors['disc_topic_text'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = DiscussionsForm()
        self.assertEqual(form.Meta.fields, ['topic', 'disc_topic_text'])


class TestDiscussionsCommentsForm(TestCase):

    def test_item_comment_is_required(self):
        form = Discussions_CommentsForm({'comment': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('comment', form.errors.keys())
        self.assertEqual(form.errors['comment'][0], 'This field is required.')

    def test_disc_comment_fields_are_explicit_in_form_metaclass(self):
        form = Discussions_CommentsForm()
        self.assertEqual(form.Meta.fields, ['comment'])
