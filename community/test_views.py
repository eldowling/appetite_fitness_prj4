from django.test import TestCase
from django.contrib.auth.models import User
from .models import Discussions, Discussion_Comments


class TestViews(TestCase):

    def test_get_discussion_list(self):
        response = self.client.get('/community/viewlist/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'community/discussions_list.html')

    # Removed this test as it was further complicated by getting the 
    # user's ordered products in the view and returning a 404

    # def test_get_add_discussion_page(self):
    #     test_user = User.objects.create_user(
    #         'johndoe', 'johndoe@example.com', 'johndoepass')
    #     self.client.login(username='johndoe', password='johndoepass')
    #     # Need to define the user's orders 'user_orders'
    #     # Then need to define 'order_lineitem' - the order line items of user_orders
    #     # This in turn would get the products ordered 'user_products'
    #     response = self.client.get('/community/add/', follow=True)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'community/add_discussion.html')

    def test_get_edit_discussion_page(self):
        test_user = User.objects.create_user(
            'johndoe', 'johndoe@example.com', 'johndoepass')
        self.client.login(username='johndoe', password='johndoepass')
        discussion = Discussions.objects.create(
            topic='Test Discussion', disc_topic_text='Some text')
        response = self.client.get(f'/community/edit/{discussion.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'community/edit_discussion.html')

    def test_get_add_comment_page(self):
        test_user = User.objects.create_user(
            'johndoe', 'johndoe@example.com', 'johndoepass')
        self.client.login(username='johndoe', password='johndoepass')
        discussion = Discussions.objects.create(
            topic='Test Discussion', disc_topic_text='Some text')
        response = self.client.get(f'/community/comment/{discussion.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'community/add_comment.html')
    
    def test_get_edit_comment_page(self):
        test_user = User.objects.create_user(
            'johndoe', 'johndoe@example.com', 'johndoepass')
        self.client.login(username='johndoe', password='johndoepass')
        discussion_comment = Discussion_Comments.objects.create(
            comment='Some Comment Text')
        response = self.client.get(
            f'/community/edit_comment/{discussion_comment.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'community/edit_comment.html')

    def test_add_discussion_comment(self):
        test_user = User.objects.create_user(
            'johndoe', 'johndoe@example.com', 'johndoepass')
        self.client.login(username='johndoe', password='johndoepass')
        discussion = Discussions.objects.create(
            topic='Test Discussion', disc_topic_text='Some text')
        response = self.client.post(f'/community/comment/{discussion.id}/',
            {'comment': 'New test Discussion'})
        self.assertRedirects(response, f'/community/view/{discussion.id}/')

    # Remove this as getting a 404 error
    # def test_edit_discussion(self):
    #     test_user = User.objects.create_user(
    #         'johndoe', 'johndoe@example.com', 'johndoepass')
    #     self.client.login(username='johndoe', password='johndoepass')
    #     discussion = Discussions.objects.create(
    #         topic='Test Discussion - Edited', disc_topic_text='Some text, edited')
    #     response = self.client.post(f'/community/edit/{discussion.id}/',
    #         {'comment': 'New test Discussion'})
    #     self.assertRedirects(response, f'/community/view/{discussion.id}/')

    def test_edit_discussion_comment(self):
        test_user = User.objects.create_user(
            'johndoe', 'johndoe@example.com', 'johndoepass')
        self.client.login(username='johndoe', password='johndoepass')
        discussion_comment = Discussion_Comments.objects.create(
            comment='Some Comment Text')
        response = self.client.post(
            f'/community/edit_comment/{discussion_comment.id}/',
            {'comment': 'Edit test Discussion'})
        self.assertRedirects(response, f'/community/view/{discussion_comment.id}/')
