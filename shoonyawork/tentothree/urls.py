from django.urls import path
# from .views import process_command
from . import views

urlpatterns = [
    path("", views.login_view, name="login"),
    path("dashboard", views.dashboard, name="dashboard"),
    # path('process_command/', process_command, name='process_command'),
    # path("tentothree/ajax/", views.tentothree_ajax_view, name="tentothree_ajax"), 
]