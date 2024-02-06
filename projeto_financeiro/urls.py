from django.contrib import admin
from django.urls import path, include

from ativos.views import index
from ativos.views import dashboard
from members.views import login_user 

urlpatterns = [
    path('admin/', admin.site.urls),

    path(
        "index/",
        index,
        name="index"
    ),

    path(
        "dashboard/",
        dashboard,
        name="dashboard"
    ),
    
    path(
        "",
        login_user,
        name="login_user"
    ),



]
