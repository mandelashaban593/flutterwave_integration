# stdlib imports

# django imports
from django.urls import path, include

# 3rd party imports

# project imports
from integration.views import plan,uganda,createplan,create_plan
from . import views

app_name = "integration"

urlpatterns = [path("", views.plan, name="plan"),
path("uganda",views.uganda,name="uganda"),
path("createplan/<str:pk>",views.createplan,name="createplan"),
path("create_plan/<str:pk>", views.create_plan, name="create_plan"),
path("login", views.login_view, name="login")]
