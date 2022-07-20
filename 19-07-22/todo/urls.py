"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from note.views import NoteListAPiView,  NoteCreateApiView,NoteListCreateAPIView,NoteRetrieveDestroyAPIView, NoteRetrieveUpdateDestroyAPIView, NoteViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('note/', NoteListAPiView.as_view()),
    path('note_create/', NoteCreateApiView.as_view()),
    path('note_create_list/',NoteListCreateAPIView.as_view()),
    path('note_destroy/<int:pk>/',NoteRetrieveDestroyAPIView.as_view()),
    path('note_destroy_2/<int:pk>/',NoteRetrieveUpdateDestroyAPIView.as_view()),
    path("otra/", include("note.urls"))
]
