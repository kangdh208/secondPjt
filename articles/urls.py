from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    path("", views.index, name="index"),
    path("details/<int:pk>/", views.detail, name="detail"),
    path("<int:pk>/comments/", views.comment_create, name="comment_create"),
    path(
        "<int:article_pk>/comments/<int:comment_pk>/delete/",
        views.comment_delete,
        name="comment_delete",
    ),
    path(
        "<int:article_pk>/comments/<int:comment_pk>/reply/",
        views.reply_create,
        name="reply_create",
    ),
    path("details/<int:pk>/bookmark/", views.bookmark, name="bookmark"),
]
