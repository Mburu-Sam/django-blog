# from django.urls import path
# from .views import post_list, post_detail

# urlpatterns = [
# path("post/<int:pk>/", post_detail, name="post_detail"),
# path("", post_list, name="home"),
# ]

# from django.urls import path
# from . import views
# urlpatterns = [
#     path("post/new/", views.BlogCreateView.as_view(), name="post_new"),
#     path("post/<int:pk>/", views.BlogDetailView.as_view(), name="post_detail"),
#     path("post/<int:pk>/edit/", views.BlogUpdateView.as_view(), name="post_edit"),
#     path("post/<int:pk>/delete/", views.BlogDeleteView.as_view(), name="post_delete"),
#     path("", views.BlogListView.as_view(), name="home"), 
# ]

from django.urls import path
from . import views

urlpatterns = [
    path("", views.BlogListView.as_view(), name="home"),

    path("post/new/",views.BlogCreateView.as_view(),name="post_new",),

    path("post/<int:pk>/",views.BlogDetailView.as_view(),name="post_detail", ),

    path("post/<int:pk>/edit/",views.BlogUpdateView.as_view(),name="post_edit",),

    path("post/<int:pk>/delete/",views.BlogDeleteView.as_view(),name="post_delete",),

    path("signup/",views.SignUpView.as_view(),name="signup",),
]