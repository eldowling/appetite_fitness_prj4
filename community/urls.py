from django.urls import path
from . import views
from .views import Discussions_List

urlpatterns = [
    path('viewlist/', Discussions_List.as_view(), name='discussions_list'),
    path('add/', views.add_discussion_topic, name='add_discussion'),
    path('view/<int:discussion_id>/', views.view_topic, name='view_topic'),
    path('comment/<int:discussion_id>/', views.add_comment, name='add_comment'),
]