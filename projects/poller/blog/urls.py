from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
	path('', views.index, name="index"),
	path('<int:post_id>/', views.view_post, name="view"),
	path('new/', views.new_post, name="new"),
	path('create/', views.create_post, name="create"),
	path('<int:post_id>/edit', views.edit_post, name="edit"),
	path('<int:post_id>/update', views.update_post, name="update"),
]