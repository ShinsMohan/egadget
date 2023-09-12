from django.urls import path
from .views import *

urlpatterns =[
    path("re",RegView.as_view(),name="re")

]