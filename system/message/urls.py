from django.urls import path
from . import views

urlpatterns = [
    
    path('sendMessage/', views.sendMessage),
    path('inbox/', views.inbox),
    path('unread-inbox/', views.unread_inbox),
    path('readMessage/<int:id>', views.readMessage),
    path('deleteMessage/<str:user>/<int:id>', views.deleteMessage),

]
