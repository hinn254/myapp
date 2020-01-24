from django.urls import path
from myapp import views


urlpatterns = [
    path("",views.index.as_view(),name="index")
]
