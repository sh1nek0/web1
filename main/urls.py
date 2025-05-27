from django.urls import path
from .views import index, thabest, feedback_view, like_post

from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', index, name='index'), 
    path('thabest/', thabest, name='thabest'),
    path('api/feedback/', feedback_view, name='feedback-api'), 
    path("like/<int:post_id>/", like_post, name="like_post"),
    
]

urlpatterns += staticfiles_urlpatterns()