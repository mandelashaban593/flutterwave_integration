# stdlib imports

# django imports
from django.urls import path, include

# 3rd party imports

# project imports
from integration.views import SignUpView

app_name = "integration"

urlpatterns = [path("", SignUpView.as_view(), name="signup")]
