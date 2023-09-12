from django.urls import path
from .views import *


urlpatterns=[
    path("cust",CustomerHomeView.as_view(),name="custhome"),
    path("pdetail/<int:id>",ProductDetailView.as_view(),name="pdet")
]