from django.urls import path
from . import views

urlpatterns = [
    # write message
    path('sendMessage/', views.sendMessage),

    # Get all messages for a specific user
    path('inbox/<str:user>', views.inbox),
]
