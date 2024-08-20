from django.urls import path
# from .views import process_command
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    # path('process_command/', process_command, name='process_command'),
]