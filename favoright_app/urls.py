 
from email.mime import base
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views_auth import handle_login, handle_logout
from .views import *

router = DefaultRouter()
router.register("posts", PostViewSet, basename="posts")
router.register("comments", CommentViewSet, basename="comments")
router.register("subcomments", SubCommentViewSet, basename="subcomments")
router.register("solvedfavor", SolvedFavorViewSet, basename="solvedfavor")
router.register("users", UserViewSet, basename="user")






urlpatterns = [
    path("", include(router.urls)),
    path("login/", handle_login),
    path("logout/", handle_logout),
    path('yelp_api/', handle_yelp_api),
    path('google_map_api', hendle_google_map_api),

]
