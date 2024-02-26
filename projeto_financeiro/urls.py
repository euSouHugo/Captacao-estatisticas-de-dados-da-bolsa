from django.contrib import admin
from django.urls import path

from django.views.generic import RedirectView
from ativos.views import index, dashboard
from members.views import login_user, create, configuration, history


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
        '', 
        RedirectView.as_view(pattern_name='login_user', permanent=False)),

   
    path(
        'login/', 
         login_user, 
         name='login_user'),

    path(
        "create/",
        create,
        name="create"
    ),
    
    path(
        "index/history/",
        history,
        name="history"
    ),
     path(
        "index/configuration/",
        configuration,
        name="configuration"
    ),


]
