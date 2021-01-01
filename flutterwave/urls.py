# stdlib  imports

# django imports
from django.urls import path, include

# 3rd party imports

# project imports
from flutterwave.views import TransactionCreateView, TransactionDetailView


app_name = "flutterwave"

urlpatterns = [
    path("transaction/", TransactionCreateView.as_view(), name="transaction_create"),
    path("<str:tx_ref>/", TransactionDetailView.as_view(), name="transaction_detail"),
]
