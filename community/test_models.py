from django.test import TestCase
from .models import Discussions, Discussion_Comments


class TestDiscussionModel(TestCase):

    def test_str(self):
        test_topic = Discussions(
            topic='Test Discussion Topic',
            disc_topic_text='Some text on this discussion topic',
        )
        self.assertEqual(str(test_topic), 'Test Discussion Topic')
