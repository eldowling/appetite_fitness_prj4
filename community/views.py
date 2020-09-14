from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse
)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .forms import DiscussionsForm, Discussions_CommentsForm
from .models import Discussions, Discussion_Comments
from profiles.models import UserProfile
from products.models import Product


class Discussions_List(ListView):
    """Create a listview of all Discussions"""
    template_name = 'community/discussions_list.html'
    queryset = Discussions.objects.all()


@login_required
def add_discussion_topic(request):
    """ Add a new discussion topic for a product """

    # product = user's purchased product - ? do in forms.py?
    if request.method == 'POST':
        if request.user.is_authenticated:
            profile = UserProfile.objects.get(user=request.user)

            form_data = {
                'product': request.POST['product'],
                'topic': request.POST['topic'],
                'disc_topic_text': request.POST['disc_topic_text'],
            }

            discussion_form = DiscussionsForm(form_data)
            if discussion_form.is_valid():
                discussion_object = discussion_form.save(commit=False)
                discussion_object.user_profile = profile
                discussion_form.save()

                return redirect('discussions_list')
            else:
                messages.error(request, 'There is an error on the form. \
                    Please review the details entered')
    else:
        discussion_form = DiscussionsForm()

    template = 'community/add_discussion.html'
    context = {
        'form': discussion_form,
    }

    return render(request, template, context)


@login_required
def edit_discussion(request, discussion_id):
    """ Edit the selected discussion topic for a product """

    discussion = get_object_or_404(Discussions, pk=discussion_id)
    if request.method == 'POST':
        if request.user.is_authenticated:
            discussion_form = DiscussionsForm(request.POST, request.FILES, instance=discussion)
            if discussion_form.is_valid():
                discussion_form.save()
                messages.success(request, 'The topic has been successfully updated')
                return redirect(reverse('view_topic', args=[discussion_id]))
            else:
                messages.error(request,
                            ('Failed to update topic. '
                                'Please ensure the form is valid.'))
    else:
        discussion_form = DiscussionsForm(instance=discussion)

    template = 'community/edit_discussion.html'
    context = {
        'form': discussion_form,
        'discussion': discussion,
    }

    return render(request, template, context)


def view_topic(request, discussion_id):
    """A view to display the discussion details for the selected topic"""

    discussion = get_object_or_404(Discussions, pk=discussion_id)
    disc_comments = Discussion_Comments.objects.filter(disc_topic=discussion_id)

    template = 'community/view_discussion.html'
    context = {
        'discussion': discussion,
        'disc_comments': disc_comments,
    }

    return render(request, template, context)


@login_required
def add_comment(request, discussion_id):
    """ Add a comment on the selected discussion topic """

    discussion = get_object_or_404(Discussions, pk=discussion_id)
    if request.method == 'POST':
        if request.user.is_authenticated:
            profile = UserProfile.objects.get(user=request.user)

            form_data = {
                'comment': request.POST['comment'],
            }

            d_comment_form = Discussions_CommentsForm(form_data)
            if d_comment_form.is_valid():
                discussion_object = d_comment_form.save(commit=False)
                discussion_object.user_profile = profile
                discussion_object.disc_topic = discussion
                d_comment_form.save()

                return redirect(reverse('view_topic', args=[discussion_id]))
            else:
                messages.error(request, 'There is an error on the form. \
                    Please review the details entered')
    else:
        d_comment_form = Discussions_CommentsForm()

    template = 'community/add_comment.html'
    context = {
        'form': d_comment_form,
        'discussion': discussion,
    }

    return render(request, template, context)


@login_required
def edit_comment(request, comment_id):
    """ Edit a commennt for the selected discussion topic """
    
    disc_comment = get_object_or_404(Discussion_Comments, pk=comment_id)
    if request.method == 'POST':
        if request.user.is_authenticated:
            d_comment_form = Discussions_CommentsForm(request.POST, request.FILES, instance=disc_comment)
            if d_comment_form.is_valid():
                d_comment_form.save()
                messages.success(request, 'The comment has been successfully updated')
                return redirect(reverse('view_topic', args=[disc_comment.disc_topic.id]))
            else:
                messages.error(request,
                            ('Failed to update comment. '
                                'Please ensure the form is valid.'))
    else:
        d_comment_form = Discussions_CommentsForm(instance=disc_comment)

    template = 'community/edit_comment.html'
    context = {
        'form': d_comment_form,
        'd_comment': disc_comment,
    }

    return render(request, template, context)
