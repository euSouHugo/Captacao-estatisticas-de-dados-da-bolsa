from django.contrib import admin
from django.urls import path, include

from ativos.views import index
from ativos.views import dashboard

urlpatterns = [
    path('admin/', admin.site.urls),

    path(
        "",
        index,
        name="index"
    ),

    path(
        "dashboard/",
        dashboard,
        name="dashboard"
    ),
    
    path(
        "members/", 
        include('django.contrib.auth.urls')
    ),

    path(
        "members/", include('members.urls')
    ),

]
