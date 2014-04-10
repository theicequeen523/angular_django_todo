"""
This is your project's master URL configuration, it defines the set of "root" URLs for the entire project
"""
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('apps.public',
                       # Rest Pattern for Todo Items
                       url(r'^api/todo/(?P<user_id>[0-9]+)$', 'views.todo_api', name="create_todo"),
                       url(r'^api/recipe/(?P<user_id>[0-9]+)$', 'views.recipe_api', name="create_recipe"),
                       url(r'^api/tag$', 'views.tag_api', name='tag_api'),

                       url(r'^user/id$', 'views.get_current_user_id', name="get_current_user_id"),
                       url(r'^todos$', 'views.todos', name="todo_list_html"),
                       url(r'^todos-django$', 'views.todos_django', name="todo_list_django"),
                       url(r'^logout$', 'views.logout', name="user_logout"),
                       url(r'^login$', 'views.login', name="user_login"),
                       url(r'^recipes$', 'views.recipe_list', name='recipe'),
                       url(r'^add_recipe$', 'views.add_recipe', name='add_recipe'),
                       url(r'^edit_recipe/(?P<pk>[0-9]+)$', 'views.edit_recipe', name='edit_recipe'),
                       url(r'^recipes/(?P<pk>[0-9]+)$', 'views.recipe_detail', name='recipe_detail'),
                       url(r'^$', 'views.home', name="home"))