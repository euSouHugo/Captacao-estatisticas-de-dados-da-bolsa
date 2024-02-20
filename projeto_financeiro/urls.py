from django.contrib import admin
from django.urls import path

from ativos.views import index, dashboard
from members.views import login_user, create

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

    path(
        "create/",
        create,
        name="create"
    ),


]
