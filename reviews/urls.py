# adapted from https://github.com/jadianes/winerama-recommender-tutorial
from django.urls import path, re_path
from  . import views

urlpatterns = [
    # ex: /
    #re_path('', views.redirect_view),
    re_path(r'^$', views.review_list, name='review_list'),
    # ex: /review/5/
    re_path(r'review/(?P<review_id>[0-9]+)/$', views.review_detail, name='review_detail'),
    # ex: /beer/
    re_path(r'^beer$', views.beer_list, name='beer_list'),
    # ex: /beer/5/
    re_path(r'^beer/(?P<beer_id>[0-9]+)/$', views.beer_detail, name='beer_detail'),

    re_path(r'^beer/(?P<beer_id>[0-9]+)/add_review//$', views.add_review, name='add_review'),

    # ex: /review/user - get reviews for the logged user
    re_path(r'^review/user/(?P<username>\w+)/$', views.user_review_list, name='user_review_list'),
    re_path(r'^review/user/$', views.user_review_list, name='user_review_list'),
    re_path(r'^recommendation/$', views.user_recommendation_list, name='user_recommendation_list'),

]
app_name = 'reviews'
