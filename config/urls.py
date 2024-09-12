"""config URL Configuration

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
from django.urls import path
from todo.views import (IndexListView, status_reverse, delete_complete_tasks, update_task, delete_task, index_json_view,  json_frontend_view)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexListView.as_view(), name='index'),
    path('task-status/<int:pk>/', status_reverse),
    path("delete_complete_tasks/", delete_complete_tasks),
    path('update-task/<int:pk>/', update_task),
    path('delete/<int:pk>/', delete_task),
    path('json_simple', index_json_view, name='index-json'),
    path('json_frontend', json_frontend_view, name='json-frontend'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
